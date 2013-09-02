import random
percent=random.random()
print ('A Fire Beast Has Appeared!')
print ('You have attack, water, grass, and fire spells! Plus mindfocus when you get low on sp!')

# Constants
global mindfocus
global fire
global water
global grass
global attack
global sp

water=50
grass=0
fire =5
attack=30
mindfocus=20

sp=50
phase=''
counter=1
fireattack=40

def batalha1():
   fireattack=45
   firebeastattack2=25
   counter=1
   firebeast=500
   p1=450
   
   if percent<0.25:
      print ('It is pouring! The fire beast is weakening!')
      firebeast-=100
      firebeastattack2-=5
      fireattack-=10
   if percent>0.25 and percent<0.5:
      print ('The sun is intensifying! The firebeast seems stronger!')
      firebeast+=25
      fireattack+=10
   if percent>0.5 and percent<0.75:
      print ('The clouds are covering the sun so it is dark! You can put all your strength in because you can see him clearly!')
      attack+=15
      p1=p1+50
   firebeast=firebeast
   p1+=200

   # Main Loop
   while p1>0 and firebeast>0:
      phase=input()
      if phase=='water':
         if sp<10:
            print ('sp too low')
            continue
         sp=sp-10
         firebeast=firebeast-water
         print(water)
      elif phase=='attack':
         firebeast=firebeast-attack
         print(attack)
      elif phase=='fire':
         if sp<10:
            print ('sp too low')
            continue
         firebeast=firebeast-fire
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
         p1=p1-fireattack
         print (fireattack)
      else:
         print ('firebeast attacked you!')
         p1=p1-firebeastattack21
         print (firebeastattack21)
      counter=counter+1 
      print ('you have', sp, 'sp remaining!')
      print ('you have', p1, 'hp remaining!')
   print(p1)
   print(firebeast)


def batalha2():
   counter=1
   firebeastattack2=25
   fireattack=50
   p1=450
   if firebeast > 0:
      print ('You Lose!')
   if p1 > 0:
      print ('You Win')
      print ('You gained the heal ability') 
      print ('you decided to go to the pond. There you found a water elemental!')
   if percent<0.25:
      print ('The sun is intensifying! The water elemental seems weaker!')
      firebeast=firebeast-25
      firebeastattack2=firebeastattack-15
      fireattack=fireattack-10
   if percent>0.25 and percent<0.5:
      print ('It is pouring! The water elemental is stronger!')
      firebeast=firebeast+25
      fireattack=fireattack+10
   if percent>0.5 and percent<0.75:
      print ('The clouds are covering the sun! The water elemental seems unaffected.')
   firebeast=firebeast+20
   p1=p1+300

   # Main Loop
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
         p1=p1-firebeastattack2+5
         print (firebeastattack2+5)
      counter=counter+1 
      print ('you have', sp, 'sp remaining!')
      print ('you have', p1, 'hp remaining!')
   print(p1)
   print(firebeast)

def batalha3():
   counter=1
   p1=450
   firebeast=600
   firebeastattack2=40
   if firebeast > 0:
      print ('You Lose!')
   if p1 > 0:
      print ('You Win') 
      print ('You gained the dodge ability') 
      print ('you decided to go to the forest. There you found a tree beast!')
   firebeast2=firebeast+30
   if percent<0.25:
      print ('The sun is intensifying! The tree beast seems to be growing rapidly!')
      firebeastattack22=firebeastattack2-15
   if percent>0.25 and percent<0.5:
      print ('It is pouring! The tree beast is stronger!')
   if percent>0.5 and percent<0.75:
      print ('The clouds are covering the sun! The tree beast will not grow!But it is to dark to dodge!.')

   # Main loop
   while p1>0 and firebeast>0:
      phase=input()
      if firebeastattack22_old: 
         firebeastattack22 = firebeastattack2_old
      if phase==dodge:
         if sp<20:
            print('sp too low')
            continue
         sp=sp-20
         firebeastattack22_old = firebeastattack2
         firebeastattack22=0
         fireattack2=0
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
         print('the tree beast grows rapidly he is too powerful!')
         p1=p1-99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
         
      elif phase=='attack':
         firebeast2=firebeast2-attack
         print(attack)
      elif phase=='fire':
         if sp<10:
            print ('sp too low')
            continue
         sp=sp-10
         firebeast2=firebeast2-water
         firebeast2=firebeast2/1.25
         firebeastattack22=firebeastattack2/2
      elif phase=='grass':
         if sp<10:
            print ('sp too low')
            continue
         sp=sp-10
         firebeast2=firebeast2-fire
      elif phase=='mindfocus':
         sp=sp+mindfocus
      else:
         print ('invalid option')
         continue
      if counter==2 or counter== 5 or counter== 6 or counter== 9:
         print ('tree beast is growing!')
         firebeast2=firebeast2*1.1
         firebeastattack22=firebeastattack2*2
      else:
         print ('water elemental attacked you!')
         p1=p1-firebeastattack22+10
         print (firebeastattack22+10)
      counter=counter+1 
      print ('you have', sp, 'sp remaining!')
      print ('you have', p1, 'hp remaining!')
   print(p1)
   print(firebeast2)
   if firebeast > 0:
      print ('You Lose!')
   if p1 > 0:
      print ('You Win')

def batalha4():
   counter=1

   print ('A mysterious voice booms through the land "DO YOU REALIZE WHAT YOU HAVE DONE THE ULTIMATE CHIMERA IS RELEASED!!!!')
   chimera=500
   p1almighty=500
   holy=100
   almightyattack=40

   # Main Loop
   while chimera>0 and p1almighty>0:
      phase=input()
      if phase==holy:
         if sp<40:
            ('sp too low')
            continue
         chimera=chimera-holy
      elif phase==attack:
         chimera =chimera-almightyattack
      elif phase==heal:
         p1almighty=p1almighty+50
      else:
         print ('invalid option')
         continue

      if counter==3 or counter==5 or counter==8 or counter==9:
         p1almighty=p1almighty-50
         print ('chimera unleashed evil upon the world!you are blinded by its force you barely felt it but you feel weaker!')
      else:
         print ('chimera unleshes several destuctive forces at you!')
         print ('20')
         print ('10')
         print ('30')
         print ('10')
         p1almighty=p1almighty-70
      counter=counter+1
   print (chimera)
   print (p1almighty)
   if chimera>0:
      print ('you lose')
   if chimera<=0:
      print ('You Have Banished The Ultimate Chimera Congratulations!')



batalha1()
batalha2()
batalha3()
batalha4()

