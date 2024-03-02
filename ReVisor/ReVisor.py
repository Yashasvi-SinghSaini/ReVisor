from customtkinter import *
from Scripts import ReVisor_funcs
import playsound
import pandas
import datetime

app = CTk()
app.geometry("1400x400")
app.wm_title("ReVisor")
app.iconbitmap("Assets/icon.ico")
app._set_appearance_mode('dark')
set_default_color_theme("blue")



def button_func():
    if Chapter.get() != '':
        if Topic.get() != '':
            csv_old=pandas.read_csv('Assets/data.csv')
            if prv_day_check.get()==0:
                data={"Date":[ReVisor_funcs.daychange(1),
                            ReVisor_funcs.daychange(8),
                            ReVisor_funcs.daychange(22),
                            ReVisor_funcs.daychange(50),
                            ReVisor_funcs.daychange(80),
                            ReVisor_funcs.daychange(110),
                            ReVisor_funcs.daychange(170),
                            ReVisor_funcs.daychange(230),
                            ReVisor_funcs.daychange(290),
                            ReVisor_funcs.daychange(370),
                            ReVisor_funcs.daychange(430),
                            ReVisor_funcs.daychange(590),
                            ReVisor_funcs.daychange(650)],
                    "Chapter":[Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get()],
                    "Topics":[(Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get())]} 
            elif prv_day_check.get() == 1:
                    data={"Date":[ReVisor_funcs.daychange(1-1),
                            ReVisor_funcs.daychange(8-1),
                            ReVisor_funcs.daychange(22-1),
                            ReVisor_funcs.daychange(50-1),
                            ReVisor_funcs.daychange(80-1),
                            ReVisor_funcs.daychange(110-1),
                            ReVisor_funcs.daychange(170-1),
                            ReVisor_funcs.daychange(230-1),
                            ReVisor_funcs.daychange(290-1),
                            ReVisor_funcs.daychange(370-1),
                            ReVisor_funcs.daychange(430-1),
                            ReVisor_funcs.daychange(590-1),
                            ReVisor_funcs.daychange(650-1)],
                    "Chapter":[Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get(), Chapter.get()],
                    "Topics":[(Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get()), (Topic.get())]} 
            csv_new=pandas.DataFrame(data)
            csv_combined = pandas.concat([csv_old, csv_new])
            csv_combined.to_csv('Assets/data.csv', index=False)
            csv_combined = pandas.read_csv('Assets/data.csv')
        else:
            CTkLabel(master=frame_1, text="Enter Doubt!!!", text_color='#b52309', font=('Commissioner', 17)).pack(pady=[0,10])
    else:
        CTkLabel(master=frame_1, text="Enter Chapter!!!", text_color='#b52309', font=('Commissioner', 17)).pack(pady=[0,10])
    Topic.delete(0, len(Topic.get()))
    playsound.playsound('Assets/btn_clck.wav')



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



frame_2 = CTkScrollableFrame(master=app, fg_color="#ff704d", border_width=5, width=700)
frame_2.grid(row=0, column=2, rowspan=3)

CTkLabel(master=frame_2, text="TOPICS TO REVISE TODAY:", text_color='#b3ffff', font=("Cascadia Mono SemiBold", 25), justify="center").pack(expand=True, pady=15, padx=20)

csv = pandas.read_csv('Assets/data.csv')

print=0
for i in range(len(csv.index)):
    if csv['Date'][i] == str(datetime.date.today()):
        data = ReVisor_funcs.shorten_doubt(csv['Topics'][i])
        doubt_check = CTkLabel(master=frame_2, text=f'➧{csv['Chapter'][i]} ⇛ {data}', text_color='#b3ffb3',font=("Cascadia Mono", 20), justify="left").pack(expand=True, pady=2, padx=10)
        print=1
if print==0:
    CTkLabel(master=frame_2, text=f'NOTHING TO REVISE TODAY!!!', text_color='#b3ffb3',font=("Cascadia Mono", 20), justify="left").pack(expand=True, pady=2, padx=10)

app.mainloop()
