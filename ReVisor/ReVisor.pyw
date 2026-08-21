from customtkinter import *
from Scripts import ReVisor_funcs
from playsound3 import playsound

app = CTk()
app.geometry("1200x400")
app.wm_title("ReVisor")
app.iconbitmap("Assets/icon.ico")
app._set_appearance_mode('dark')
set_default_color_theme("blue")



def button_func():
    if Chapter.get() != '':
        if '___' not in Chapter.get():
            if Topic.get() != '':
                if '___' not in Topic.get():
                    ReVisor_funcs.rev_topic__insert(Chapter.get(), Topic.get(), prv_day_check.get())
                    Topic.delete(0, len(Topic.get()))
                    playsound.playsound('Assets/btn_clck.wav')
                else:
                    underscore_error = CTkLabel(master=frame_1, text="Don't Use ___ in topic name",text_color='#ff0000', width=400, font=("Cascadia Mono", 18))
                    underscore_error.pack(expand=True, pady=6, padx=2)
            else:
                topic_error = CTkLabel(master=frame_1, text="ENTER TOPIC!!!",text_color='#ff0000', width=400, font=("Cascadia Mono", 18))
                topic_error.pack(expand=True, pady=6, padx=2)
                
        else:
            underscore_error = CTkLabel(master=frame_1, text="Don't Use ___ in chapter name",text_color='#ff0000', width=400, font=("Cascadia Mono", 18))
            underscore_error.pack(expand=True, pady=6, padx=2)
    else:
        chap_error = CTkLabel(master=frame_1, text="ENTER CHAPTER!!!",text_color='#ff0000', width=400, font=("Cascadia Mono", 18))
        chap_error.pack(expand=True, pady=6, padx=2)



frame_1 = CTkFrame(master=app, fg_color="#ff9900", border_width=5)
frame_1.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=50, pady=50)

study_head = CTkLabel(master=frame_1, text='WHAT DID YOU STUDY TODAY', text_color='#ccddff', font=("Cascadia Mono SemiBold", 25), justify="center")
Chapter = CTkEntry(master=frame_1, placeholder_text="Chapter?",text_color='#ffb3ff', width=400, font=("Cascadia Mono", 15))
Topic = CTkEntry(master=frame_1, placeholder_text="Topic?",text_color='#ffb3ff', width=400, font=("Cascadia Mono", 15))
button = CTkButton(master=frame_1, text="Add", command=button_func, font=("Cascadia Mono", 15))
prv_day_check = CTkCheckBox(master=frame_1, text="Add for previous day?", font=("Cascadia Mono", 15), corner_radius=20, fg_color='#ff3333', checkmark_color='#66ff33', text_color='#ffe6e6', checkbox_width=30, hover_color='#ff4d4d')


def today_yester_study():
    if prv_day_check.get()==0:
        study_head.configure(text="WHAT DID YOU STUDY TODAY")
    elif prv_day_check.get()==1:
        study_head.configure(text="WHAT DID YOU STUDY YESTERDAY") 

prv_day_check.configure(command=today_yester_study)

study_head.pack(expand=True, pady=(30, 15), padx= 20)
prv_day_check.pack()
Chapter.pack(expand=True, pady=15, padx=20)
Topic.pack(expand=True, pady=15, padx=20)
button.pack(expand=True, fill="both", pady=(30, 15), padx=30)



frame_2 = CTkFrame(master=app, fg_color="#ff704d", border_width=5)
frame_2.grid(row=0, column=2, rowspan=3)

CTkLabel(master=frame_2, text="TOPICS TO REVISE TODAY:", text_color='#b3ffff', font=("Cascadia Mono SemiBold", 25), justify="center").pack(expand=True, pady=15, padx=20)
CTkLabel(master=frame_2, text=ReVisor_funcs.rev_topic__get(), text_color='#b3ffb3',font=("Cascadia Mono", 20), justify="left").pack(expand=True, pady=15, padx=20)

app.mainloop()
