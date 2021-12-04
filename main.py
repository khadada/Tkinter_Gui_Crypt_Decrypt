from tkinter import *
from tkinter import ttk
bg_color = '#00BBF9'
STND_FONT =('Arial', 12, "italic")
TITLE_FONT =('Arial',20, "bold")
CPYRIGHT_FONT =('Arial',9, "normal")
window = Tk()
window.title('Khaled Program')
window['background'] = bg_color
window.attributes('-alpha',0.9)
window.minsize(900,600)
label = Label(window,text='encode decode message '.title(), font=TITLE_FONT,bg=bg_color)
label.pack()
#------------------------------------------------------------------
labe_name = Label(window,text='Full Name: ', font=STND_FONT,bg=bg_color)
labe_name.place(x=10,y=80)
input_name = Entry(window, borderwidth=10, relief=FLAT,width=40, font=STND_FONT)
input_name.place(x=100,y=70)
#------------------------------------------------------------------
email_label = Label(window,text='Email: ', font=STND_FONT,bg=bg_color)
email_label.place(x=10,y=150)
email = Entry(window, borderwidth=10, relief=FLAT,width=40,font=STND_FONT)
email.place(x=100,y=140)
#------------------------------------------------------------------
label = Label(window,text='Message: ', font=STND_FONT,bg=bg_color)
label.place(x=10,y=210)
message = Text(window, borderwidth=10, relief=FLAT,width=40,font=STND_FONT ,height=10)
message.place(x=100,y=210)
#------------------------------------------------------------------
crypt_button = Button(text="Crypt Message",font=STND_FONT,bg='#FFC107',width=15,pady=5,fg='#000',border=0,activebackground='#222',activeforeground='#fff')
crypt_button.place(x=100,y=450)

#------------------------------------------------------------------
decrypt_button = Button(text="Decrypt Message",font=STND_FONT,bg='#F76F8E',width=15,pady=5,fg='#000',border=0,activebackground='#222',activeforeground='#fff')
decrypt_button.place(x=340,y=450)
#------------------------------------------------------------------
label_output = Label(window,text='Result: ', font=STND_FONT,bg=bg_color)
label_output.place(x=510,y=210)
text_output = Text(window, borderwidth=10, relief=FLAT,width=40,font=STND_FONT ,height=10)
text_output.place(x=600,y=210)
#------------------------------------------------------------------
cpright = Label(window,text='Crypt_Decrypt program by khaled melizi all copyright © 2021 preserved ', font=CPYRIGHT_FONT,bg=bg_color)
cpright.pack(side="bottom")




window.mainloop()