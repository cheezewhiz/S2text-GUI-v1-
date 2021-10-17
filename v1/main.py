from tkinter import*
import cv2
from PIL import Image,ImageTk
top = Tk()
top.geometry("700x700")

button_start=Button(top,text="START",pady="20",padx="30",activebackground="grey",activeforeground="white",relief=GROOVE,
                    cursor="tcross",borderwidth=5)
button_start.pack(pady=40)
video_frame=LabelFrame(top,bg="grey",relief=RIDGE, borderwidth = 5)
video_frame.place(x=40, y=170)
vid=Label(video_frame,height="250",width="250")
vid.pack(side="left")
output_frame=Frame(top,bg="grey",height="250",width="250",relief=RIDGE, borderwidth = 5)
output_frame.place(x=400, y=170)

canvas= Canvas(top, width= 700, height= 200)
canvas.pack()

#Load an image in the script
img= (Image.open("ASLimage.jpg"))

#Resize the Image using resize method
resized_image= img.resize((500,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(100,-10, anchor=NW, image=new_image)
canvas.place(relx=0.0, rely=1.0, anchor=SW)
cap=cv2.VideoCapture(0)

while True:
    img=cap.read()[1]
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img=ImageTk.PhotoImage(Image.fromarray(img))
    vid['image']=img
    top.update()