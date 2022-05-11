from pprint import pprint #meilleur affichage du print
import re
import json

ipcount = {}
codecount = {}

with open("./access.log", "r") as file_pointer:  #lire le fichier par ligne
    lines = file_pointer.readlines()
    regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.+\] \".+\" (\d{3}) \d+ "  #regex pour trouver l'addresse ip et le code status
    for l in lines :  #boucle pour chaque ligne appliquer le regex 
        ip , code = re.findall(regex, l)[0]

        if ip not in ipcount:     #créé un dico pour chaque ip si le dico n'existe pas
            ipcount[ip] = {}
        
        if code in ipcount[ip]:   #si le code est dans le dico de l'ip l'ajouter
            ipcount[ip][code] += 1
        else:                      #sinon faire +1 au compteur de ce code
            ipcount[ip][code] = 1

with open ("ipstatus.json", "w") as json_file_pointer:   #créé le fichier json de tout ce parser
    json.dump(ipcount, json_file_pointer, indent=2)