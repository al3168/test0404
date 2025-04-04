# # Crea un sistema ripetibile che si occupi di dividere su tre possibili liste i tipi basilari di dato che riceve in entrata. Deve poter stampare una lista singola o tutte.  Si deve ripetere X volte definite all'inizio dall'utente


lista1 =[ 3]
list2=["strina"]
lista3= [True]

while True :
    richiesta=int(input ("dammi un tipo di dato"))## prendo l input
    if richiesta == int:
        print(richiesta.append(lista1)) ## 
       
    elif richiesta == "str":
        print(richiesta.append(list2))
        
    elif richiesta == "True" or "False":
        print(richiesta.append(lista3))
    else:
        print("ci spiaace la selezione non è corretta ")
        break
    
    
    
 #Andare a creare un sistema ripetibile che si occupa di gestire la lunghezza delle stringhe e salvarle, l'utente potrà continuare a inserire dati finché la stringa inserita e più lunga della precedente, alla fine stamperà l'insieme delle stringhe date in input divise da virgole e quante stringhe ha inserito.
lista=[]
while True :
    richiesta = input("inserisci una stringa ")
    richiesta2 = input("inserisci una stringa ")
    if len(richiesta2) > len(richiesta) : ##uso len per verificare la lunghezza delle stringhe 
        print(" perfetto possiamo continua dammi un altra stringa")
    else :
        print("ci spiace non puoi proseguire ")
        
      
        ### ho un buco non riesco a ricordare come salvare  ti scrivo il finale che che dovrebbe stampare tutte quelle salvate ovviamente commentata
        ##  print(lista)
