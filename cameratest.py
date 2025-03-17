import cv2
import numpy as np
from ultralytics import YOLO
from tracker import Tracker# Import your tracker module here
import pandas as pd
import cvzone
import urllib.request
#import controller as cnt
#import time
model = YOLO('yolov8s.pt')

coordinates = []

def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        coordinates.clear()
        coordinates.append((x, y))
        print(f"Coordinates: {x}, {y}")

cv2.namedWindow('Video 1')
cv2.setMouseCallback('Video 1', get_coordinates)

cv2.namedWindow('Video 2')
cv2.setMouseCallback('Video 2', get_coordinates)
url1='http://192.168.211.227/cam-mid.jpg'
url2='http://192.168.211.135/cam-mid.jpg'

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
#print(class_list)

tracker1 = Tracker()
tracker2 = Tracker()

tracker3 = Tracker()
tracker4 = Tracker()
tracker5=  Tracker()

area1 = [(271, 203), (328, 273), (586, 231), (483, 177)]
area2 = [(323, 232), (304, 349), (470, 336), (432, 229)]  # Define area for video 2
count=0
len1car={}
len1truck={}

len1carcounter=[]

len1truckcounter=[]
len2car={}
len2truck={}

len2carcounter=[]
len2truckcounter=[]


while True:
   try:
      response1 = urllib.request.urlopen(url1)  # Set a timeout for the connection attempt
      img_array1 = np.array(bytearray(response1.read()), dtype=np.uint8)
      frame1 = cv2.imdecode(img_array1, -1)
      frame1 = cv2.resize(frame1, (1020, 500))

      response2 = urllib.request.urlopen(url2)  # Set a timeout for the connection attempt
      img_array2 = np.array(bytearray(response2.read()), dtype=np.uint8)
      frame2 = cv2.imdecode(img_array2, -1)
      frame2 = cv2.resize(frame2, (1020, 500))
      list1=[]
      list2=[]
      list3=[]
      list4=[]
      
      results1 = model.predict(frame1)
      # print(results1)
      a=results1[0].boxes.data
      px1=pd.DataFrame(a).astype("float")
      #print(px1)
      for index, row in px1.iterrows():
          #print(row)
        
          x1=int(row[0])
          y1=int(row[1])
          x2=int(row[2])
          y2=int(row[3])
          d=int(row[5])
          c=class_list[d]
          if 'car' in c:
              list1.append([x1,y1,x2,y2])
          
          elif'truck' in c:
              list2.append([x1,y1,x2,y2])
          
      
      bbox1_id = tracker1.update(list1)
      bbox2_id= tracker2.update(list2)
      
      
 ####################len1bus############################   
      for bbox1 in bbox1_id:
           x3, y3, x4, y4, id1 = bbox1
           cx1 = int(x3 + x4) // 2
           cy1 = int(y3 + y4) // 2
           results1 = cv2.pointPolygonTest(np.array(area1, np.int32), ((cx1, cy1)), False)
           if results1 >= 0:
            
        
              cv2.circle(frame1,(cx1,cy1),4,(255,0,255),-1)
              cv2.rectangle(frame1,(x3,y3),(x4,y4),(255,0,0),2)
              cvzone.putTextRect(frame1,f'{id1}',(x3,y3),1,1)
              if len1carcounter.count(id1)==0:
                  len1carcounter.append(id1)
#######################len1truck#####################################            
      for bbox2 in bbox2_id:
          x5, y5, x6, y6, id2 = bbox2
          cx2 = int(x5 + x6) // 2
          cy2 = int(y5 + y6) // 2
          results1 = cv2.pointPolygonTest(np.array(area1, np.int32), ((cx2, cy2)), False)
          if results1 >= 0:
            
        
              cv2.circle(frame1,(cx2,cy2),4,(255,0,255),-1)
              cv2.rectangle(frame1,(x5,y5),(x6,y6),(255,0,0),2)
              cvzone.putTextRect(frame1,f'{id2}',(x5,y5),1,1)
              if len1truckcounter.count(id2)==0:
                  len1truckcounter.append(id2)
                  
     
    
      results2 = model.predict(frame2)
      #print(results2)
      b=results2[0].boxes.data
      px2=pd.DataFrame(b).astype("float")
      #print(px2)
      for index, row in px2.iterrows():
           #print(row)
         
        
        
          x1=int(row[0])
          y1=int(row[1])
          x2=int(row[2])
          y2=int(row[3])
          d=int(row[5])
          c=class_list[d]
          if 'car' in c:
              list3.append([x1,y1,x2,y2])
          
          elif'truck' in c:
               list4.append([x1,y1,x2,y2])
         
    
      bbox3_id = tracker3.update(list3)
      bbox4_id= tracker4.update(list4)
      
      
################len1truck#########################
      for bbox3 in bbox3_id:
          x7, y7, x8, y8, id3 = bbox3
          cx3 = int(x7 + x8) // 2
          cy3 = int(y7 + y8) // 2
          results2 = cv2.pointPolygonTest(np.array(area2, np.int32), ((cx3, cy3)), False)
          if results2 >= 0:
            
        
             cv2.circle(frame2,(cx3,cy3),4,(255,0,255),-1)
             cv2.rectangle(frame2,(x7,y7),(x8,y8),(255,0,0),2)
             cvzone.putTextRect(frame2,f'{id3}',(x7,y7),1,1)
             if len2carcounter.count(id3)==0:
                 len2carcounter.append(id3)
######################len2truck######################
    
      for bbox4 in bbox4_id:
          x9, y9, x10, y10, id4 = bbox4
          cx4 = int(x5 + x6) // 2
          cy4 = int(y5 + y6) // 2
          results2 = cv2.pointPolygonTest(np.array(area2, np.int32), ((cx4, cy4)), False)
          if results2 >= 0:
            
        
             cv2.circle(frame2,(cx4,cy4),4,(255,0,255),-1)
             cv2.rectangle(frame2,(x9,y9),(x10,y10),(255,0,0),2)
             cvzone.putTextRect(frame2,f'{id4}',(x9,y9),1,1)
             if len2truckcounter.count(id4)==0:
                 len2truckcounter.append(id4)
                 
      
#####################counter################################    
      cv2.polylines(frame1,[np.array(area1,np.int32)],True,(255,255,0),3)
      cv2.polylines(frame2,[np.array(area2,np.int32)],True,(255,255,0),3)
      
        
      clen1=len(len1carcounter)
      clen2=len(len2carcounter)
      tlen1=len(len1truckcounter)
      tlen2=len(len2truckcounter)
      
      len1totalcounter= clen1 + tlen1
      len2totalcounter= clen2 + tlen2
      #cnt.led(len1totalcounter,len2totalcounter)
#################video show###################################    
      cvzone.putTextRect(frame1,f'len1car:-{clen1}',(50,60),1,1)
      cvzone.putTextRect(frame1,f'len1truck:-{tlen1}',(786,50),1,1)
      
      
      cvzone.putTextRect(frame2,f'len2car:-{clen2}',(50,60),1,1)
      cvzone.putTextRect(frame2,f'len2truck:-{tlen2}',(771,50),1,1)
      
      cv2.imshow("Video 1", frame1)
    
      cv2.imshow("Video 2", frame2)

      if cv2.waitKey(1) & 0xFF == 27:
        break
  
   except urllib.error.URLError as e:
        print(f"URLError occurred: {e}")
        # Handle specific URL-related errors here, such as incorrect URL or network issues.

   except Exception as ex:
        print(f"Error occurred: {ex}")
        # Handle any other unexpected exceptions that may occur.


cv2.destroyAllWindows()


