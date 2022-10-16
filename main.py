import fitz # install using: pip install PyMuPDF
import string
import re
import nltk
nltk.download('all')
from nltk import sent_tokenize,word_tokenize
from nltk.corpus import stopwords  #stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
stemmer=PorterStemmer()
from wordcloud import WordCloud
import matplotlib.pyplot as plt



def return_doc_from_bytes(pdfbytes):
  doc = fitz.open(stream=pdfbytes)
  return doc

def preprocessing(sentences):
  documents_clean = ''
  for d in sentences:
      # Remove Unicode
      document_test = re.sub('[^a-zA-Z0-9]', ' ', d)
      # Lowercase the document
      document_test = document_test.lower()
      # Remove punctuations
      document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)
      #Remove the numbers
      document_test = re.sub(r'[0-9]', '', document_test)
      # Remove the doubled space
      document_test = re.sub(r'\s{2,}', ' ', document_test)
      #tokenization
      document_test = document_test.split()
      #stopwords_removal
      document_test = [word for word in document_test if not word in set(stopwords.words('english'))]
      #stemming
      #document_test = [stemmer.stem(word) for word in document_test]
      #lemmmitization
      document_test = [lemmatizer.lemmatize(word) for word in document_test]
      document_test = ' '.join(document_test)
      documents_clean+=(document_test)
  # print(documents_clean)


def get_wordcloud():
  st.set_page_config(layout = "wide")
  st.title("Word Cloud of supply contract")
  fileupload = st.sidebar.file_uploader("Upload a Contract here")
  Button=st.sidebar.button('Get wordcloud')
   
  if fileupload is not None:
    text=''
    
    pdfbytes = fileupload.getvalue()
    doc = return_doc_from_bytes(pdfbytes)
    for page in doc:
      text+=(page.get_text()
    sentences = nltk.sent_tokenize(text)
    cleaned_document=preprocessing(sentences)
    wordcloud = WordCloud(width = 800, height =600,background_color ='white',min_font_size = 5,max_words=500).generate(cleaned_document)
    # plot the WordCloud image                      
    plt.figure(figsize = (15,10), facecolor = None)
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)

    plt.show()
 

if __name__ == "__main__":
    get_wordcloud()
