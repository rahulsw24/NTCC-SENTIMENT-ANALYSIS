#cleaning text steps
# 1) Create a text file and take text from it.
# 2) Convert the letter into lowercase.
# 3) Remove Punctuations.
import string
text = open('read.txt',encoding='UTF-8').read()
lower_case = text.lower()
#str.maketrans Parameters
#str1 - Specifies the list of characters that needs to be deleted.
#str2 - Specifies the list of characters with which it needs to be replaced.
#str3 - Specifies the list of characters that needs to be deleted.
clean_text = lower_case.translate(str.maketrans('','',string.punctuation))
print(clean_text)
#Tokenisation - breaking of sentences into words.
#Words stored in the form of a list.
tokenized_words=clean_text.split()
print(tokenized_words)
#stopwords - Dont add any meaning to any sentences.
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#Removing Stop words
final_words = []
for word in tokenized_words: 
    if word not in stop_words:
        final_words.append(word)
print (final_words)       
 


