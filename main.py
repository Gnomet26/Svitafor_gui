import tkinter as tk
import time
from threading import Thread
from tkinter import messagebox

class Svitafor_gui:

    def __init__(self):
        #======================= Variables ==================================

        self.is_run:bool = False
        self.reverse_ = False
        self.red_light = True
        self.yellow_light = False
        self.green_light = False

        self.red_light_time = 0
        self.yellow_light_time = 0
        self.green_light_time = 0

        self.red_interval_time = 0
        self.yellow_interval_time = 0
        self.green_interval_time = 0

        #========================== Init window ===================================

        self.oyna = tk.Tk()
        self.oyna.geometry("300x460")
        self.oyna.title("Svetofor")
        self.oyna.resizable(False,False)

        #===================== Canvas window ======================================

        self.my_Canvas = tk.Canvas(master=self.oyna,width=298,height=358,bg="#272727")
        self.my_Canvas.place(x = 0,y = 0)

        #======================= Colors ==========================================

        self.my_oval_red = self.my_Canvas.create_oval(109,30,189,110,fill="#000000")

        self.my_oval_yellow = self.my_Canvas.create_oval(109, 140, 189, 220, fill="#000000")

        self.my_oval_green = self.my_Canvas.create_oval(109, 250, 189, 330, fill="#000000")

        #============================== Widgets ==========================================

        self.red_interval = tk.Entry(self.oyna,width=3,font=("Arial",16),justify="center",bg="#ff3f3f")
        self.red_interval.place(x = 20,y = 368)

        self.yellow_interval = tk.Entry(self.oyna, width=3, font=("Arial", 16), justify="center", bg="#ffff2b")
        self.yellow_interval.place(x=130, y=368)

        self.green_interval = tk.Entry(self.oyna, width=3, font=("Arial", 16), justify="center", bg="#38ff28")
        self.green_interval.place(x=230, y=368)

        self.start_button = tk.Button(master=self.oyna,font=("Arial",20),text="Start",bd=2,padx=30,command=lambda :self.begin_loop_th())
        self.start_button.place(x = 10,y = 410)

        self.stop_button = tk.Button(master=self.oyna, font=("Arial", 20), text="Stop", bd=2, padx=30,command=lambda :self.stop_loop())
        self.stop_button.place(x=170, y=410)
        self.oyna.bind("<Destroy>",lambda x:self.close_app())
        self.oyna.update()
        self.oyna.mainloop()

    def updater(self):
        if self.is_run :
            if self.red_light:
                if not self.reverse_:
                    if (self.red_interval_time >= self.red_light_time):
                        self.my_Canvas.itemconfig(self.my_oval_red,fill = "#ff1212")
                        self.my_Canvas.itemconfig(self.my_oval_yellow,fill = "#000000")
                        self.my_Canvas.itemconfig(self.my_oval_green, fill="#000000")

                        self.red_light_time += 1
                    else:

                        self.red_light = False
                        self.yellow_light = True
                        self.green_light = False

                        self.red_light_time = 0
                        self.yellow_light_time = 0
                        self.green_light_time = 0

                else:
                    if (self.red_interval_time >= self.red_light_time):
                        self.my_Canvas.itemconfig(self.my_oval_red, fill="#ff1212")
                        self.my_Canvas.itemconfig(self.my_oval_yellow, fill="#000000")
                        self.my_Canvas.itemconfig(self.my_oval_green, fill="#000000")

                        self.red_light_time += 1
                    else:

                        self.red_light = False
                        self.yellow_light = True
                        self.green_light = False
                        self.reverse_ = False

                        self.red_light_time = 0
                        self.yellow_light_time = 0
                        self.green_light_time = 0

            elif self.yellow_light:
                if not self.reverse_:
                    if (self.yellow_interval_time >= self.yellow_light_time):
                        self.my_Canvas.itemconfig(self.my_oval_red, fill="#000000")
                        self.my_Canvas.itemconfig(self.my_oval_yellow, fill="#ffff12")
                        self.my_Canvas.itemconfig(self.my_oval_green, fill="#000000")

                        self.yellow_light_time += 1
                    else:

                        self.red_light = False
                        self.yellow_light = False
                        self.green_light = True

                        self.red_light_time = 0
                        self.yellow_light_time = 0
                        self.green_light_time = 0
                else:
                    if (self.yellow_interval_time >= self.yellow_light_time):
                        self.my_Canvas.itemconfig(self.my_oval_red, fill="#000000")
                        self.my_Canvas.itemconfig(self.my_oval_yellow, fill="#ffff12")
                        self.my_Canvas.itemconfig(self.my_oval_green, fill="#000000")

                        self.yellow_light_time += 1
                    else:

                        self.red_light = True
                        self.yellow_light = False
                        self.green_light = False

                        self.red_light_time = 0
                        self.yellow_light_time = 0
                        self.green_light_time = 0
            elif self.green_light:
                if not self.reverse_:
                    if (self.green_interval_time >= self.green_light_time):
                        self.my_Canvas.itemconfig(self.my_oval_red, fill="#000000")
                        self.my_Canvas.itemconfig(self.my_oval_yellow, fill="#000000")
                        self.my_Canvas.itemconfig(self.my_oval_green, fill="#12ff12")

                        self.green_light_time += 1
                    else:

                        self.red_light = False
                        self.yellow_light = True
                        self.green_light = False
                        self.reverse_ = True

                        self.red_light_time = 0
                        self.yellow_light_time = 0
                        self.green_light_time = 0

            time.sleep(1)
            self.updater()

    def begin_loop_th(self):

        try:

            if not self.is_run:

                self.red_interval_time = int(self.red_interval.get())
                self.yellow_interval_time = int(self.yellow_interval.get())
                self.green_interval_time = int(self.green_interval.get())

                if(self.red_interval_time == 0 or self.yellow_interval_time == 0 or self.green_interval_time == 0):
                    messagebox.showinfo("Diqqat","0 interval kirita olmaysiz!")

                else:
                    self.is_run = True
                    th = Thread(target=lambda :self.updater())
                    th.start()
        except:
            messagebox.showerror("Diqqat","Maydon bo'sh bo'lishi mumkin emas va faqat raqam kiriting!")


    def stop_loop(self):
        self.is_run= False

        self.my_Canvas.itemconfig(self.my_oval_red, fill="#000000")
        self.my_Canvas.itemconfig(self.my_oval_yellow, fill="#000000")
        self.my_Canvas.itemconfig(self.my_oval_green, fill="#000000")

        self.red_light = True
        self.yellow_light = False
        self.green_light = False

        self.red_light_time = 0
        self.yellow_light_time = 0
        self.green_light_time = 0

    def close_app(self):
        self.is_run = False

if __name__ == "__main__":
    Svitafor_gui()