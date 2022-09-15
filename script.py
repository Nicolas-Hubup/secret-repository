str1='Patron'
page='-'
print('\n'.join
 ([''.join
   ([(str1[(x-y)%len(str1) ]
     if((x*0.05)**2+(y*0.1)**2-1)
      **3-(x*0.05)**2*(y*0.1)
       **3<=0 else page)
        for x in range(-30,30)])
         for y in range(15,-15,-1)]))
