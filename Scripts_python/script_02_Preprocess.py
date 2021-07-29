# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------
# Nom : script_04_Preprocess.py (Python version 3.x)
# Creation : 28/07/2021
# Auteur(s) : Jéros VIGAN 
# Projet : Nettoye des mots
# Description : nettoyage et recupertion des mots qui ont un sens
# ---------------------------------------------------------------------------
"""

### ===============================================================
### Prétraitement (nettoyage, reconding et normalisation)
### ===============================================================

#anglais
def Preprocess_list_anglais(listofSentence):
    # Importation des packages
    import nltk
    from nltk import word_tokenize
    from nltk.stem import WordNetLemmatizer
    import string
    from datetime import datetime
    
    # Début du programme
    debut = datetime.now()
    
    # initialisation
    nltk.download('stopwords') 
    nltk.download('punkt')
    nltk.download('words')
    nltk.download('wordnet')
    
    # settings
    stopwords = nltk.corpus.stopwords.words('english')
    words = set(nltk.corpus.words.words())
    lemmatizer = WordNetLemmatizer()
    preprocess_list = []
    
    for sentence in listofSentence :
        
        sentence_w_punct = "".join([i.lower() for i in sentence if i not in string.punctuation])
        
        sentence_w_num = ''.join(i for i in sentence_w_punct if not i.isdigit())

        tokenize_sentence = word_tokenize(sentence_w_num)
        
        words_w_stopwords = [i for i in tokenize_sentence if i not in stopwords]
        
        words_lemmatize = (lemmatizer.lemmatize(w) for w in words_w_stopwords)

        sentence_clean = ' '.join(w for w in words_lemmatize if w.lower() in words or not w.isalpha())
        
        preprocess_list.append(sentence_clean)
        
    # Fin du programme
    print(" ")
    print(f'La durée de traitement est {str(datetime.now()-debut)} s')
    
    return preprocess_list 


# french
def Preprocess_list_french(listofSentence,dicto='dictionnaire.txt'):
    # Importation des packages
    import nltk
    from nltk import word_tokenize
    from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
    from datetime import datetime
    import string
    
    # Début du programme
    debut = datetime.now()
    
    # initialisation
    nltk.download('stopwords') #mots les plus fréquents
    nltk.download('punkt')
    nltk.download('words')
    nltk.download('wordnet')

    # settings
    stopwords = nltk.corpus.stopwords.words('french')
    words = set(line.strip() for line in open(dicto,encoding="utf8"))
    lemmatizer = FrenchLefffLemmatizer()
    preprocess_list = []
    
    for sentence in listofSentence :
        
        sentence_w_punct = "".join([i.lower() for i in sentence if i not in string.punctuation])
        
        sentence_w_num = ''.join(i for i in sentence_w_punct if not i.isdigit())

        tokenize_sentence = word_tokenize(sentence_w_num)
        
        words_w_stopwords = [i for i in tokenize_sentence if i not in stopwords]
        
        words_lemmatize = (lemmatizer.lemmatize(w) for w in words_w_stopwords)

        sentence_clean = ' '.join(w for w in words_lemmatize if w.lower() in words or not w.isalpha())
        
        preprocess_list.append(sentence_clean)
        
    # Fin du programme
    print(" ")
    print(f'La durée de traitement est {str(datetime.now()-debut)} s')
    
    return preprocess_list 


