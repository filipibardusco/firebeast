import random
percent=random.random()
print ('A Fire Beast Has Appeared!')
print ('You have attack, water, grass, and fire spells! Plus mindfocus when you get low on sp!')
water=50
grass=0
fire =5
attack=30
sp=50
mindfocus=20
p1=450
firebeast=500
phase=''
counter=1
firebeastattack=25
fireattack=40
if percent<0.25:
   print ('It is pouring! The fire beast is weakening!')
   firebeast=firebeast-100
   firebeastattack=firebeastattack-5
   fireattack=fireattack-10
if percent>0.25 and percent<0.5:
   print ('The sun is intensifying! The firebeast seems stronger!')
   firebeast=firebeast+25
   fireattack=fireattack+10
if percent>0.5 and percent<0.75:
   print ('The clouds are covering the sun so it is dark! You can put all your strength in because you can see him clearly!')
   attack=attack+15
   p1=p1+50
firebeast1= firebeast
while p1>0 and firebeast1>0:
   phase=input()
   if phase=='water':
      if sp<10:
         print ('sp too low')
         continue
      sp=sp-10
      firebeast1=firebeast1-water
      print(water)
   elif phase=='attack':
      firebeast1=firebeast1-attack
      print(attack)
   elif phase=='fire':
      if sp<10:
         print ('sp too low')
         continue
      firebeast1=firebeast1-fire
      sp=sp-10
      print(fire)
   elif phase=='grass':
      if sp<10:
         print ('sp too low')
         continue
      sp=sp-10
      print ('the firebeast explodes in flames!')
      p1=p1-999999999999999999999999999999999999999999999999999999999999999999999999999999999
   elif phase=='mindfocus':
      sp=sp+mindfocus
   else:
      print ('invalid option')
      continue
   if counter==2 or counter== 5 or counter== 6 or counter== 9:
      print ('firebeast did a fire attack!')
      p1=p1-fireattack1
      print (fireattack1)
   else:
      print ('firebeast attacked you!')
      p1=p1-firebeastattack1
      print (firebeastattack1)
   counter=counter+1 
   print ('you have', sp, 'sp remaining!')
   print ('you have', p1, 'hp remaining!')
print(p1)
print(firebeast1)
if firebeast1 > 0:
   print ('You Lose!')
if p1 > 0:
   print ('You Win')
   print ('You gained the heal ability')
print ('you decided to go to the pond. There you found a water elemental!')
if percent<0.25:
   print ('The sun is intensifying! The water elemental seems weaker!')
   firebeast=firebeast-25
   firebeastattack=firebeastattack-15
   fireattack=fireattack-10
if percent>0.25 and percent<0.5:
   print ('It is pouring! The water elemental is stronger!')
   firebeast=firebeast+25
   fireattack=fireattack+10
if percent>0.5 and percent<0.75:
   print ('The clouds are covering the sun! The water elemental seems unaffected.')
while p1>0 and firebeast>0:
   firebeast=firebeast
   firebeast = firebeast+30
   phase=input()
   if phase=='heal':
      if sp<20:
         print('sp too low')
         continue
      p1=p1+30
      sp=sp-20
   elif phase=='water':
      if sp<10:
         print ('sp too low')
         continue
      sp=sp-10
      firebeast=firebeast-fire
      print(fire)
   elif phase=='attack':
      firebeast=firebeast-attack
      print(attack)
   elif phase=='fire':
      if sp<10:
         print ('sp too low')
         continue
      print ('The water elemental turned to a smoke elemental! You cannot see it attacks will miss!')
      p1=p1-999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
   elif phase=='grass':
      if sp<10:
         print ('sp too low')
         continue
      sp=sp-10
      firebeast=firebeast-water
   elif phase=='mindfocus':
      sp=sp+mindfocus
   else:
      print ('invalid option')
      continue
   if counter==2 or counter== 5 or counter== 6 or counter== 9:
      print ('water elemental did a tsunami attack!')
      p1=p1-fireattack+5
      print (fireattack+5)
   else:
      print ('water elemental attacked you!')
      p1=p1-firebeastattack+5
      print (firebeastattack+5)
   counter=counter+1 
   print ('you have', sp, 'sp remaining!')
   print ('you have', p1, 'hp remaining!')
print(p1)
print(firebeast)
if firebeast > 0:
   print ('You Lose!')
if p1 > 0:
   print ('You Win')
