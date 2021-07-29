# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------
# Nom : script_04_Text_To_Speech.py (Python version 3.x)
# Creation : 28/07/2021
# Auteur(s) : Jéros VIGAN 
# Projet : Audio 
# Description : lire et enregistrer en format audio
# ---------------------------------------------------------------------------
"""
def text_to_speech(text,language ='en', name="read_article.mp3"):
    # Importation des packages
    from gtts import gTTS
    import os
    from datetime import datetime
    
    # Début du programme
    debut = datetime.now()
    
    myobj = gTTS(text, lang=language, slow=False)
    myobj.save(name)
    os.system("start "+ name)
    
    # Fin du programme
    print(" ")
    print(f'La durée de traitement est {str(datetime.now()-debut)} s')