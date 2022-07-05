import cv2 as cv
from simple_facerec import SimpleFacerec#module to comapre real time video with images in directory.

simp=SimpleFacerec()#creating an object of simpleFacerec.

simp.load_encoding_images('images')#calling a definition and loading images floder path can also be added and it prints
# total number of images in the passed direcory.

fname=0
key=0
floca=0
img=cv.VideoCapture(0)#to open inbuild face cam(0) and capture real time video frame by frame.

while True:#untill user don't want to exit program will not end.

    ret,fram=img.read()#reading the captured image frame,fram will recieve coordinates of from user img\video..

    floca,fname=simp.detect_known_faces(fram)
#SimpleFacerec has a definition detect_known_face where the image frame will be passed and will be compared
#with the images in the image directory and will return the name of that has matched and the coordinates.

    for location,name in zip(floca,fname):
#Location will get the coordinates of user face i.e real time video and name will be assigned name of the
#image which has matched.

        y,x,y1,x1=location[0],location[1],location[2],location[3]
#location will be assigned four cordinates of user face from real time video.and now these coordinates will
#be assigned to four individual variables x,y,x1,y1.

        cv.putText(fram,name,(y,x),cv.FONT_ITALIC,1,(0,0,800),2)
#now cv2 has a () with which text can be displayed on screen in this case we want to print name of user if face is found
# else unknown will be printed.
        cv.rectangle(fram,(x,y),(x1,y1),(0,0,200),4)
#rectangle will be formed on these coordinates.
        if cv.waitKey(1) & 0xFF == ord(' '):
#when user will press space bar program will be ended i.e exit\quit.
            quit(0)
    cv.imshow('Frame', fram)
    key=cv.waitKey(1)