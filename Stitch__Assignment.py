import cv2

filename = "/Users/suhaanshaik/Desktop/Minecraft_stitch_test.mp4"
cap = cv2.VideoCapture(filename)

Chosen_Frames = []
Frame_Tracker = 0

if not cap.isOpened(): #Brief Error loop to see if there is an issue with opening the file
    print("The video file couldn't be opened") 


while cap.isOpened():
    Successful, frame = cap.read() 

    if not Successful: #Once we have got all the frames we need, we stop collecting more video data
        break

    if Frame_Tracker % 60 == 0: #60 Frames keeps the code flowing by reducing how many images go through the stitcher
        Chosen_Frames.append(frame)

    Frame_Tracker += 1

cap.release()

print(f"This loop has finished. We collected {len(Chosen_Frames)} frames") #Just verifying how many frames we collected

stitching = cv2.Stitcher_create(cv2.Stitcher_SCANS)

Condition, Minecraft_Map = stitching.stitch(Chosen_Frames)

print("The Stitching Function is done processing now!") #If the Stitching Function processed correctly, this outputs

if Condition == cv2.Stitcher_OK:
    cv2.imwrite("/Users/suhaanshaik/Desktop/Minecraft_world_map.jpg", Minecraft_Map) #Have this new Minecraft map be placed in my Desktop as a jpg file
    print("We Successfully created our Minecraft Map") #See if the final Map is created 
else:
    print(f"Something's wrong with the Stitching The error code is {Condition}") #If the final map isn't created, there's something wrong. 

