import  random
ol=[random.randint(-15,15) for _  in range (10)]
print(ol)
sq=list(map(lambda x:x*x,ol))
print(sq)
