import random
ma_list =["anne","aline","gros","eve","armand","yves","elv","allo","sonia","luc","marc","jules","kevin"]
#this will contain an occurence of our list
maListOc = ma_list
#this list will contain our random list
random_list = None
groupe = 1
#for each element in ma_list, we randome and put into our variable
for i in ma_list:
#This condition will avoid errors when n is greater than 4
    if(len(ma_list)<=5): # ici au lieu de 5 Monsieur a fait exprés et il a remplacé par 6
        break
    random_list = random.sample(ma_list, 5)
    #then we remove data already randomize in our list, but the complexity is high for this little program
    for element in random_list:
        ma_list.remove(element)
    print("Goupe N°:",groupe)
    #and we finally print our randomized list
    print(random_list)
    print("__________________________________________")
    groupe += 1
print("Goupe N°:",groupe)
print(maListOc)
