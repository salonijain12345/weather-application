from tkinter import*
from tkinter.font import BOLD
from PIL import Image,ImageTk
import w
import requests 
apii_key = w.api_key
class myweather:
    def __init__(self,root):
        self.root=root
        self.root.title("my weather app")
        #self.root.iconbitmap('search.png')
        self.root.geometry('350x400+350+100')
        self.root.config(bg="white")
        #=====variable=====
        self.var_search=StringVar() 
        #===icon==========
        self.search_icon=Image.open("C:/Users/Administrator/Desktop/python projects/search.png")
        self.search_icon=self.search_icon.resize((28,25),Image.ANTIALIAS)
        self.search_icon=ImageTk.PhotoImage(self.search_icon)
        
        title=Label(self.root,text='weather app',font=("goudy old style",30,'bold'),bg="#247326",fg="white").place(x=0,y=0,relwidth=1,height=60)
        lbl_city=Label(self.root,text='City Name',font=("goudy old style",15),bg="#033958",fg="white",anchor='w',padx=5).place(x=0,y=60,relwidth=1,height=40)
        txt_city=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightgreen",fg="#262626").place(x=100,y=68,width=200,height=25)
        btn_search=Button(self.root,cursor="hand2",image=self.search_icon,activebackground="#033958",bd=1,bg="#033958",command=self.get_weather).place(x=310,y=68,width=30,height=25)

        #=========results==============
        self.lbl_city=Label(self.root,font=("goudy old style",15,'bold'),bg="white",fg="green")
        self.lbl_city.place(x=0,y=110,relwidth=1,height=20)
        
        self.lbl_icons=Label(self.root,font=("goudy old style",15,'bold'),bg="white",)
        self.lbl_icons.place(x=0,y=135,relwidth=1,height=100)
        
        self.lbl_temp=Label(self.root,font=("goudy old style",15,'bold'),bg="white",fg="orange")
        self.lbl_temp.place(x=0,y=250,relwidth=1,height=20)
        
        self.lbl_wind=Label(self.root,font=("goudy old style",15,'bold'),bg="white",fg="#262626")
        self.lbl_wind.place(x=0,y=270,relwidth=1,height=20)
        
        self.lbl_error=Label(self.root,font=("goudy old style",20,'bold'),bg="white",fg="red")
        self.lbl_error.place(x=0,y=300,relwidth=1,height=30)

        #======footer=======
        self.lbl_footer=Label(self.root,text='Developed by Saloni',font=("goudy old style",15),bg="#033958",fg="white",pady=5).pack(side=BOTTOM,fill=X)
        
        
    def get_weather(self):
            apii_key=w.api_key
            complete_url=f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={apii_key}"
            # city name ,country name,temp_c,temp_f,wind
            if self.var_search.get()=="":
                self.lbl_error.config(text="city name required")
                self.lbl_city.config(text="")
                self.lbl_icons.config(image="")
                self.lbl_temp.config(text="")
                self.lbl_wind.config(text="") 
            else:   
                result=requests.get(complete_url)
                if result:
                    json=result.json()
                    city_name=json['name']
                    country=json['sys']["country"]
                    icons=json["weather"][0]['icon']
                    temp_c=(json['main']["temp"]-273.15)
                    temp_f=(json['main']["temp"]-273.15) *9/5+32
                    wind=json["weather"][0]["main"]
                    self.lbl_city.config(text=city_name+','+country)
                    
                    deg=u"\N{DEGREE SIGN}"
                    self.lbl_temp.config(text=str(round(temp_c,2))+deg+"c |"+ str(round(temp_f,2))+deg+" F")
                    self.lbl_wind.config(text=wind)
                    self.lbl_error.config(text='')
                
                else:
                    self.lbl_city.config(text="")
                    self.lbl_icons.config(image="")
                    self.lbl_temp.config(text="")
                    self.lbl_wind.config(text="") 
                    self.lbl_error.config(text="invalid city ")   
                
                

root=Tk()        
obj=myweather(root)
root.mainloop()