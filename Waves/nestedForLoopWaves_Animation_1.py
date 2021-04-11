# settings
fill(1,1,1)
rect(0,0,width(), height())
shift = 60
offset = 200
# program
# for x in range(10):
#     for y in range(10):
#         fill(random(), random(), random())
#         #translate(10+y)
#         #rotate(10*x)
#         rect(offset + x * shift, offset + y * shift, shift, shift)
# for x in range(10):
# #for y in range(10):
#     fill(.1*x,0,.1*x,.2)
#     #translate(159*x,-133*x)
#     #rotate(10*x)
#     rect(offset + x * shift, offset, shift, shift)
    
#WORKING!!!:   
# for x in range(10):
# #for y in range(10):
#     with savedState():
#         fill(.1*x,0,.1*x)
#         #translate(0*x,45*x)
#         rotate(-10*x, center=(offset + x * shift+.5*shift,offset + .5*shift))
#         rect(offset + x * shift, offset, shift, shift)
for i in range(60):  
    fill(0,0,0)
    rect(0,0,width(), height())  
    for x in range(10):
        for y in range(10):
            with savedState():
                

                fill(.5,.01*x-.1*y,.1*y)
                #translate(0*x,45*x)
                rotate(50+6*i+x*y, center=(offset + x * shift+.5*shift,offset + y * shift+.5*shift))
                rect(offset + x * shift, offset + y * shift, shift, shift)
                #saveImage("myFirstMultipageScript(3).jpg")
    
    if i < 59:
        newPage()
        
saveImage("Animation_Squares(8).mp4")