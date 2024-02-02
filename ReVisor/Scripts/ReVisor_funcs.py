import datetime

date_today=datetime.date.today() 

def dayadd(days_to_add): #THIS FUNCTION ADDS GIVEN DAYS TO A DATE
    return date_today + datetime.timedelta(days_to_add)
def str_add(old_str, to_add_text, index): #THIS FUNCTION INSERTS A SUBSTRING TO A EXISTING STRING
    newstr=old_str[0:index] + to_add_text +'\n' + old_str[index:]
    return newstr

def rev_topic__insert(topic, subtopic):
    with open('Assets/rdate.yashasvi', 'a') as file_append: #IN THIS ITERATION WE INSERT NEW ENTRIES IN DATABASE
        adding_day=[1,8,22,50,100,150,200,250,300] #REVISION GAP 

        for i in adding_day: 
            with open('Assets/rdate.yashasvi', 'r') as file_read:
                date_data = file_read.read() #READS THE DATA OF rdate.ext

            if str(dayadd(i)) in date_data: #CHECKS IF DATE ENTRY ALREADY EXISTS IN DATABASE
                index_existing_date = date_data.find(str(dayadd(i))) #FINDS THE INDEX OF EXISTING DATE ENTRY IN rdate.yashasvi

                with open('Assets/rdate.yashasvi', 'w') as file_write:  
                    file_write.write(str_add(date_data, f'•{topic} ===> {subtopic}', index_existing_date+13)) #INSERTS NEW TOPIC IN DATE ENTRY IN rdate.yashasvi 

            else:
                file_append.write(f"$$${dayadd(i)}$$$•{topic} ===> {subtopic}") #INSERTS NEW DATE ENTRY IN rdate.text
def rev_rem():
    with open('Assets/rdate.yashasvi', 'r') as file_read:
        date_data = file_read.read() #READS THE DATA OF rdate.ext
        for i in range(1, len(date_data.split('$$$')), 2): #BREAKS DATA IN LIST AND SEPARATES OUT DATE ENTRIES
            if date_data.split('$$$')[i]==str(date_today): #CHECKS IF A DATE ENTRY IS TODAY'S DATE 
                return date_data.split('$$$')[i+1]
