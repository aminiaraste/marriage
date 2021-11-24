import random

boys = ["ali","sam","javid","david","jak","joe"]
girls = ["sara","mary","yas","mia","nazi","pari"]
marriage = []
random.shuffle(girls)
for i in range (len(girls)):
    marriage.append([boys[i],girls[i]])
print(marriage)


