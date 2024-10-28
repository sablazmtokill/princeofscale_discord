import random


firstNames = ["Amaterasu", "Sora", "Emperor", "Hiroshi", "Amethyst", "Playada", "Adaptive", "Rebellious", "Yamato", "Dagon", "Katsu", "Saint", 
"Chrome", "Manera", "Arata", "Phantom", "Mamora", "Shirou", "Infused", "Jeffrey", "Shadow", "Neri", "Nik", "Kizaru", "Ernesto", "Richard", "Sergio", 
"Alvaro", "Leonardo", "Marco", "Katana", "Cristopher", "River", "Salvatore", "Kelly", "Britney", "Alessandro", "Francesco", "Ichigo", "Lucas", "Amalion", 
"Kichiro", "Martin", "Chase", "Lancelot", "James", "Taddeo", "Titled"]

lastNames = ["Edge", "Tatsuki", "Cartier", "Explorer", "Blacksimens", "Cult", "Castle", "Bennett", "Cho", "Northside", "Eternal", "Devilside", "Destruction", 
"Murasaki", "Violence", "Recovery", "Armano", "Takeda", "Soyama", "Hellwalker", "Skywalker", "Wayne", "Hennessy", "Columb", "Laurent", "Fearless", "Williams", "Murphy", 
"Hayashi", "Nakata", "Cardinal", "Agressive", "Rose", "Quinfrize", ""]

def nickname():
    nckm = str(random.choice(firstNames) + "_" + random.choice(lastNames))
    return nckm