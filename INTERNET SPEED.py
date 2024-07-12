from tkinter import * 
import speedtest 

def speedcheck():
    st = speedtest.Speedtest()
    st.get_servers()
    down = str(round(st.download() / (10**6), 3)) + " Mbps"
    up = str(round(st.upload() / (10**6), 3)) + " Mbps"
    lab_download.config(text=down)
    lab_upload.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="black")

lab = Label(
    sp,
    text="Internet Speed Test",
    font=("Time New Roman", 30, "bold"),
    bg="black",
    fg="white"
)
lab.place(x=60, y=40, height=50, width=380)

lab = Label(
    sp,
    text="Download Speed",
    font=("Time New Roman", 30, "bold")
)
lab.place(x=60, y=130, height=50, width=380)

lab_download = Label(
    sp,
    text="00",
    font=("Time New Roman", 30, "bold")
)
lab_download.place(x=60, y=200, height=50, width=380)

lab = Label(
    sp,
    text="Upload Speed",
    font=("Time New Roman", 30, "bold")
)
lab.place(x=60, y=290, height=50, width=380)

lab_upload = Label(
    sp,
    text="00",
    font=("Time New Roman", 30, "bold")
)
lab_upload.place(x=60, y=360, height=50, width=380)

button = Button(
    sp,
    text="<--- CHECK SPEED --->",
    font=("Time New Roman", 30, "bold"),
    relief=RAISED,
    bg="white",
    command=speedcheck
)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()