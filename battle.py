p1=25
p1attack=5
monster=30
monsterattack=3
counter=1
while ( monster > 0 and p1 > 0):
   monster= monster-p1attack
   p1= p1-monsterattack
   counter= counter +1
   if counter > 2:
      monster=monster-1
      if counter>4:
         monster=  monster-1
   if counter > 4 :
      p1= p1 -3
print (p1)
print (monster)
if monster<=0:
   print ('p1 wins')
if p1<=0: 
   print ('monster wins')
