import sys


a = ('    #    ',
     '   # #   ',
     '  #####  ',
     ' #     # ',
     '#       #')

b = ('######## ',
     '#       #',
     '######## ',
     '#       #',
     '######## ')
	 
c = ('#########',
     '#        ',
     '#        ',
     '#        ',
     '#########')

d = ('######## ',
     '#       #',
     '#       #',
     '#       #',
     '######## ')

e = ('#########',
     '#        ',
     '#########',
     '#        ',
     '#########')
	 
f = ('#########',
     '#        ',
     '######   ',
     '#        ',
     '#        ')
	 
g = (' ########',
     '#        ',
     '#   #### ',
     '#       #',
     ' ####### ')
	 
h = ('#       #',
     '#       #',
     '#########',
     '#       #',
     '#       #')
	 
i = ('#########',
     '    #    ',
     '    #    ',
     '    #    ',
     '#########')

j = ('#########',
     '    #    ',
     '    #    ',
     '#   #    ',
     ' ###     ')
	 
k = ('#       #',
     '#      # ',
     '#######  ',
     '#      # ',
     '#       #')
     
l = ('#        ',
     '#        ',
     '#        ',
     '#        ',
     '#########')
	 
m = ('##     ##',
     '# #   # #',
     '#  ###  #',
     '#       #',
     '#       #') 

n = ('###     #',
     '# #     #',
     '#  #    #',
     '#   #   #',
     '#    ####')

o = (' ####### ',
     '#       #',
     '#       #',
     '#       #',
     ' ####### ')
	 
p = ('#########',
     '#       #',
     '#########',
     '#        ',
     '#        ')
	 
q =  (' ####### ',
      '#       #',
      '#    #  #',
      '#     # #',
      ' ####### ')

r = ('######## ',
     '#       #',
     '######## ',
     '#    ##  ',
     '#      ##')
	 
s = (' ########',
     '#        ',
     ' ####### ',
     '        #',
     '######## ')
	 
t = ('#########',
     '    #    ',
     '    #    ',
     '    #    ',
     '    #    ')

u = ('#       #',
     '#       #',
     '#       #',
     '#       #',
     ' ####### ')
	 
v = ('#       #',
     ' #     # ',
     '  #   #  ',
     '   # #   ',
     '    #    ')
w = ('#       #',
     '#       #',
     '#  ###  #',
     '#  ###  #',
     '#### ####')
     
x = ('#       #',
     ' #     # ',
     '  #####  ',
     ' #     # ',
     '#       #')

y = ('#       #',
     ' #     # ',
     '  #####  ',
     '   ###   ',
     '   ###   ')
     
z = ('#########',
     '     ### ',
     '    ###  ',
     '   ###   ',
     '  ###    ',
     '#########')
	 
	 
#A dictionary which maps character to their tuples.	 
mylist = {'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,
	  'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,
	  'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,
	  'y':y,'z':z} 

#first argument of the command line
#So it will not read space separated name in command line
try:
	name = sys.argv[1]
except NameError:
    print('Usage: banner.py [name] without brackets.')
    sys.exit('No Input was given to the program.')
else:
    name = sys.argv[1]
itr = 0 
coloumn = 0
while itr < 5:
#Iteration is taken as five because the display I use is 5 segment display tuple.
	line = []
	
	for i in name.lower():
		line.append(mylist[i][coloumn])
	
	coloumn += 1
	print('  '.join(line))
	
	itr += 1
