import customtkinter as ct
from PIL import Image
import cv2
import face_recognition
import os
import json


def sw_com():
    global mode
    if mode == 'dark':
        ct.set_appearance_mode('light')
        mode = 'light'
    else:
        ct.set_appearance_mode('dark')
        mode = 'dark'


def info():
    backframe1 = ct.CTkFrame(app, fg_color='#011E33', width=468, height=500, corner_radius=0,
                             bg_color=('#C7EAFC', '#011E33'))
    backframe1.place(relx=0.65, rely=0.5, anchor='center')

    info_text = ct.CTkLabel(app, text='Your Information', font=('josefin sans bold', 30),
                            bg_color=('#C7EAFC', '#011E33'))
    info_text.place(relx=0.62, rely=0.2, anchor='center')

    name_text = ct.CTkLabel(app, text='Your name  :  'f'{first_1}'+' '+f'{last_1}', font=('josefin sans bold', 18),
                            bg_color=('#C7EAFC', '#011E33'))
    name_text.place(relx=0.3, rely=0.4, anchor='nw')

    username_text = ct.CTkLabel(app, text='Your Username  :  'f'{name}', font=('josefin sans bold', 18),
                                bg_color=('#C7EAFC', '#011E33'))
    username_text.place(relx=0.3, rely=0.5, anchor='nw')

    email_text = ct.CTkLabel(app, text='Your Email  :  'f'{email_1}', font=('josefin sans bold', 18),
                             bg_color=('#C7EAFC', '#011E33'))
    email_text.place(relx=0.3, rely=0.6, anchor='nw')

    ieee = ct.CTkLabel(app, text=" ", image=ieee_image, bg_color=('#C7EAFC', '#011E33'))
    ieee.place(relx=0.6, rely=0.89)


def main_page():

    backframe = ct.CTkFrame(app, fg_color='#011E33', width=702, height=500)
    backframe.place(relx=0.5, rely=0.5, anchor='center')

    list_frame = ct.CTkFrame(backframe, width=150, height=470, fg_color='#002740')
    list_frame.place(relx=0.024, rely=0.03, anchor='nw')

    logo_label = ct.CTkLabel(list_frame, text="", image=logo)
    logo_label.place(relx=0.50, rely=0.17, anchor='center')

    btn1 = ct.CTkButton(list_frame, text='Overview',
                        height=40, width=130, corner_radius=10, command=main_page,
                        font=('josefin sans medium', 20))
    btn1.place(relx=0.5, rely=0.40, anchor='center')

    btn_info = ct.CTkButton(list_frame, text='Info',
                            height=40, width=130, corner_radius=10, command=info,
                            font=('josefin sans medium', 20))
    btn_info.place(relx=0.5, rely=0.6, anchor='center')

    btn_logout = ct.CTkButton(list_frame, text='Log Out',
                              height=40, width=130, corner_radius=10,
                              font=('josefin sans medium', 20), fg_color='#ff5959',
                              command=welcome, hover_color='#840000')
    btn_logout.place(relx=0.5, rely=0.93, anchor='center')

    welcome_text = ct.CTkLabel(backframe, text='Welcome to OAAA', font=('josefin sans bold', 30),
                               bg_color=('#C7EAFC', '#011E33'))
    welcome_text.place(relx=0.62, rely=0.2, anchor='center')

    the_name = ct.CTkLabel(backframe, text=f'{first_1}'+' '+f'{last_1}', font=('josefin sans bold', 30),
                           bg_color=('#C7EAFC', '#011E33'))
    the_name.place(relx=0.62, rely=0.3, anchor='center')

    ieee = ct.CTkLabel(backframe, text=" ", image=ieee_image, bg_color=('#C7EAFC', '#011E33'))
    ieee.place(relx=0.6, rely=0.89)


def signin():
    def capture_sgn():

        global name, email_1, first_1, last_1

        name = enter_name.get()

        count = 0
        for user in d['Accounts']:
            if user['Username'] == name:
                filename = os.path.join('Accounts', f'{name}.png')
                if os.path.isfile(filename):
                    email_1 = user['Email']
                    first_1 = user['First']
                    last_1 = user['Last']
                    count = 0
                    break
            else:
                count += 1
                pass

        if count > 0:
            wrong_label = ct.CTkLabel(frm_sgn, text='Wrong! Check the spelling and try again',
                                      text_color='#B80F0A', font=('josefin sans bold', 18),
                                      bg_color=('#C7EAFC', '#011E33'))
            wrong_label.place(relx=0.65, rely=0.65, anchor='center')

            new_user_label = ct.CTkLabel(frm_sgn,
                                         text='-----------------------------------------------------------\n New User?',
                                         font=('josefin sans light', 15), bg_color=('#C7EAFC', '#011E33'))
            new_user_label.place(relx=0.65, rely=0.75, anchor='center')

            sign_up = ct.CTkButton(frm_sgn, text='Sign Up Now !',
                                   height=30, width=50, corner_radius=10, text_color='#00BBBD',
                                   font=('josefin sans bold', 15), command=signup,
                                   bg_color=('#C7EAFC', '#011E33'), fg_color=('#C7EAFC', '#011E33'),
                                   hover_color=('#C7EAFC', '#011E33'), )
            sign_up.place(relx=0.65, rely=0.85, anchor='center')
        else:
            name_new = f'{name}_new'

            cap = cv2.VideoCapture(0)

            while True:
                ret, frame = cap.read()

                cv2.imshow('Smile!', frame)
                if cv2.waitKey(1) & 0xFF == ord('\r'):
                    cv2.imwrite(f'{name_new}.png', frame)
                    account_photo = os.path.join('Accounts', f'{name}.png')
                    img = cv2.imread(account_photo)
                    bgr_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img_encode = face_recognition.face_encodings(bgr_img)[0]

                    img1 = cv2.imread(f"{name_new}.png")
                    bgr_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
                    img_encode1 = face_recognition.face_encodings(bgr_img1)[0]

                    result = face_recognition.compare_faces([img_encode], img_encode1)
                    print("result: ", result)
                    if str(result) == "[True]":
                        main_page()
                    else:
                        wrong_label = ct.CTkLabel(frm_sgn, text='Wrong! you are not ' + enter_name.get(),
                                                  text_color='#B80F0A', font=('josefin sans bold', 15),
                                                  bg_color=('#C7EAFC', '#011E33'))
                        wrong_label.place(relx=0.65, rely=0.65, anchor='center')

                    os.remove(f"{name_new}.png")
                    cap.release()
                    cv2.destroyAllWindows()
                    break
#                else:
#                    pass

    frm_sgn = ct.CTkFrame(app, fg_color='#011E33', width=702, height=500)
    back_ground2 = ct.CTkLabel(frm_sgn, text='', image=background, width=702, height=500)
    back_ground2.place(relx=0.5, rely=0.5, anchor='center')
    frm_sgn.place(relx=0.5, rely=0.5, anchor='center')
    sgn_title = ct.CTkLabel(frm_sgn, text='Sign  in  OAAA !', font=('josefin sans bold', 30),
                            bg_color=('#C7EAFC', '#011E33'))
    sgn_title.place(relx=0.65, rely=0.1, anchor='center')
    what_name = ct.CTkLabel(frm_sgn, text='Enter Your Username, Please.', font=('josefin sans bold', 15),
                            bg_color=('#C7EAFC', '#011E33'))
    what_name.place(relx=0.65, rely=0.2, anchor='center')
    enter_name = ct.CTkEntry(frm_sgn, placeholder_text='for ex "User123"',
                             height=50, width=200, corner_radius=10,
                             font=('josefin sans medium', 15),
                             text_color='#C7EAFC', placeholder_text_color='#80AAD4',
                             fg_color=('#2C80D4', '#123654'), bg_color=('#C7EAFC', '#011E33'), border_color='#80AAD4')
    enter_name.place(relx=0.65, rely=0.30, anchor='center')
    capture_login = ct.CTkButton(frm_sgn, text='Capture Face!',
                                 height=70, width=200, corner_radius=10,
                                 font=('josefin sans bold', 20), command=capture_sgn, bg_color=('#C7EAFC', '#011E33'))
    capture_login.place(relx=0.65, rely=0.50, anchor='center')

    switch_mode = ct.CTkSwitch(app, text="Switch Mode", progress_color=('#123456', '#123456'), command=sw_com,
                               fg_color='#123456', bg_color=('#C7EAFC', '#011E33'), text_color=('#011E33', '#C7EAFC'))
    switch_mode.place(relx=0.9, rely=0.95, anchor='center')

    goback1 = ct.CTkButton(frm_sgn, text='Back',
                           height=30, width=100, corner_radius=10,
                           font=('josefin sans bold', 20), command=welcome, fg_color='#B80F0A',
                           bg_color=('#C7EAFC', '#011E33'))
    goback1.place(relx=0.10, rely=0.92, anchor='center')

    ieee = ct.CTkLabel(frm_sgn, text=" ", image=ieee_image, bg_color=('#C7EAFC', '#011E33'))
    ieee.place(relx=0.76, rely=0.91)


def signup():
    def capture_sgp():
        name1 = enter_user.get()
        first = enter_first.get()
        last = enter_last.get()
        email = enter_email.get()

        def validate_user_input(username, the_email, firstname, lastname):
            for field in [username, the_email, firstname, lastname]:
                if not field.strip():
                    return False
            return True

        if validate_user_input(name1, email, first, last):
            count = 0
            new_account = {
                "Username": f"{name1}",
                "Email": f"{email}",
                "First": f"{first}",
                "Last": f"{last}"
            }

            for user in d['Accounts']:

                if user['Username'] == name1:
                    user['Email'] = email
                    user['First'] = first
                    user['Last'] = last

                    with open("data.json", "w") as data_file:
                        json.dump(d, data_file, indent=4)
                    count = 0
                    break
                else:
                    count += 1
                    pass
            if count > 0:
                d['Accounts'].append(new_account)

                with open("data.json", "w") as data_file:
                    json.dump(d, data_file, indent=4)

            cap = cv2.VideoCapture(0)

            while True:
                ret, frame = cap.read()
                cv2.putText(frame, 'Press \'Enter\' to take photo                         Press \'q\' to exit', (50, 450),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.imshow('Smile!', frame)
                if cv2.waitKey(1) & 0xFF == 13:
                    filename = os.path.join('Accounts', f'{name1}.png')
                    cv2.imwrite(filename, frame)
                    frm_done = ct.CTkFrame(app, fg_color='#011E33', width=500, height=450,
                                           corner_radius=0, bg_color=('#C7EAFC', '#011E33'))
                    frm_done.place(relx=0.77, rely=0, anchor='n')
                    sgp_done = ct.CTkLabel(frm_done, text='The Account Created\nSuccessfully!',
                                           font=('josefin sans bold', 25),
                                           bg_color=('#C7EAFC', '#011E33'),
                                           text_color='#03C04A')
                    sgp_done.place(relx=0.4, rely=0.4, anchor='center')

                    sgn_button = ct.CTkButton(frm_done, text='Sign In!', font=('josefin sans medium', 20),
                                              corner_radius=10,
                                              width=200, height=50, command=signin, bg_color=('#C7EAFC', '#011E33'))
                    sgn_button.place(relx=0.4, rely=0.6, anchor='center')
                    break
                elif cv2.waitKey(1) & 0xFF == ord('q'):
                    frm_not_done = ct.CTkFrame(app, fg_color='#011E33', width=500, height=450,
                                               corner_radius=0, bg_color=('#C7EAFC', '#011E33'))
                    frm_not_done.place(relx=0.77, rely=0, anchor='n')
                    sgp_not_done = ct.CTkLabel(frm_not_done, text='The account was NOT created!',
                                               font=('josefin sans bold', 25),
                                               bg_color=('#C7EAFC', '#011E33'),
                                               text_color='red')
                    sgp_not_done.place(relx=0.4, rely=0.4, anchor='center')

                    try_button = ct.CTkButton(frm_not_done, text='Try Again', font=('josefin sans medium', 20),
                                              corner_radius=10,
                                              width=200, height=50, command=signup, bg_color=('#C7EAFC', '#011E33'))
                    try_button.place(relx=0.4, rely=0.6, anchor='center')
                    break
            cap.release()
            cv2.destroyAllWindows()
        else:
            blank_error = ct.CTkLabel(frm_sgp, text='You Must Fill The Blanks',
                                      font=('josefin sans bold', 15), text_color='red',
                                      bg_color=('#C7EAFC', '#011E33'))
            blank_error.place(relx=0.675, rely=0.85, anchor='center')

    frm_sgp = ct.CTkFrame(app, fg_color='#011E33', width=702, height=500)
    frm_sgp.place(relx=0.5, rely=0.5, anchor='center')

    back_ground3 = ct.CTkLabel(frm_sgp, text='', image=background, width=702, height=500)
    back_ground3.place(relx=0.5, rely=0.5, anchor='center')

    sgp_title = ct.CTkLabel(frm_sgp, text='Register to Our Community!', font=('josefin sans bold', 28),
                            bg_color=('#C7EAFC', '#011E33'))
    sgp_title.place(relx=0.68, rely=0.08, anchor='center')

    name_first = ct.CTkLabel(frm_sgp, text='First Name', font=('josefin sans bold', 15),
                             bg_color=('#C7EAFC', '#011E33'))
    name_first.place(relx=0.5, rely=0.15, anchor='center')

    enter_first = ct.CTkEntry(frm_sgp, placeholder_text='"Bill"',
                              height=50, width=120, corner_radius=10,
                              font=('josefin sans medium', 15),
                              text_color=('#C7EAFC', '#C7EAFC'), placeholder_text_color='#80AAD4',
                              fg_color=('#2C80D4', '#123654'), bg_color=('#C7EAFC', '#011E33'), border_color='#80AAD4')
    enter_first.place(relx=0.44, rely=0.18, anchor='nw')

    name_last = ct.CTkLabel(frm_sgp, text='Last Name', font=('josefin sans bold', 15), bg_color=('#C7EAFC', '#011E33'))
    name_last.place(relx=0.8, rely=0.15, anchor='center')

    enter_last = ct.CTkEntry(frm_sgp, placeholder_text='"Gates"',
                             height=50, width=120, corner_radius=10,
                             font=('josefin sans medium', 15),
                             text_color=('#C7EAFC', '#C7EAFC'), placeholder_text_color='#80AAD4',
                             fg_color=('#2C80D4', '#123654'), bg_color=('#C7EAFC', '#011E33'), border_color='#80AAD4')
    enter_last.place(relx=0.74, rely=0.18, anchor='nw')

    name_user = ct.CTkLabel(frm_sgp, text='User Name', font=('josefin sans bold', 15), bg_color=('#C7EAFC', '#011E33'))
    name_user.place(relx=0.5, rely=0.34, anchor='center')

    enter_user = ct.CTkEntry(frm_sgp, placeholder_text='"B i l l . G a t e s"',
                             height=50, width=330, corner_radius=10,
                             font=('josefin sans medium', 15),
                             text_color=('#C7EAFC', '#C7EAFC'), placeholder_text_color='#80AAD4',
                             fg_color=('#2C80D4', '#123654'), bg_color=('#C7EAFC', '#011E33'), border_color='#80AAD4')
    enter_user.place(relx=0.44, rely=0.37, anchor='nw')

    name_email = ct.CTkLabel(frm_sgp, text='Your Email', font=('josefin sans bold', 15),
                             bg_color=('#C7EAFC', '#011E33'))
    name_email.place(relx=0.5, rely=0.52, anchor='center')

    enter_email = ct.CTkEntry(frm_sgp, placeholder_text='"billgates@microsoft.com"',
                              height=50, width=330, corner_radius=10,
                              font=('josefin sans medium', 15),
                              text_color=('#C7EAFC', '#C7EAFC'), placeholder_text_color='#80AAD4',
                              fg_color=('#2C80D4', '#123654'), bg_color=('#C7EAFC', '#011E33'), border_color='#80AAD4')
    enter_email.place(relx=0.44, rely=0.55, anchor='nw')

    capture_signup = ct.CTkButton(frm_sgp, text='Capture Face!',
                                  height=60, width=200, corner_radius=10,
                                  font=('josefin sans bold', 20), command=capture_sgp,
                                  bg_color=('#C7EAFC', '#011E33'))
    capture_signup.place(relx=0.675, rely=0.75, anchor='center')

    switch_mode = ct.CTkSwitch(app, text="Switch Mode", progress_color='#123456', command=sw_com,
                               fg_color='#123456', bg_color=('#C7EAFC', '#011E33'), text_color=('#011E33', '#C7EAFC'))
    switch_mode.place(relx=0.9, rely=0.95, anchor='center')

    goback2 = ct.CTkButton(frm_sgp, text='Back',
                           height=30, width=100, corner_radius=10,
                           font=('josefin sans bold', 20), command=welcome, fg_color='#B80F0A',
                           bg_color=('#C7EAFC', '#011E33'))
    goback2.place(relx=0.10, rely=0.92, anchor='center')

    ieee = ct.CTkLabel(frm_sgp, text=" ", image=ieee_image, bg_color=('#C7EAFC', '#011E33'))
    ieee.place(relx=0.76, rely=0.91)


def welcome():
    frm_welcome = ct.CTkFrame(app, fg_color='#011E33', width=702, height=500)

    back_ground = ct.CTkLabel(frm_welcome, text=" ", image=background, width=702, height=500)

    back_ground.place(relx=0.5, rely=0.5, anchor='center')
    frm_welcome.place(relx=0.5, rely=0.5, anchor='center')

    welcome_label = ct.CTkLabel(frm_welcome, text='Welcome to OAAA !', font=('josefin sans bold', 30),
                                bg_color=('#C7EAFC', '#011E33'))
    welcome_label.place(relx=0.65, rely=0.1, anchor='center')

    lgn_button = ct.CTkButton(frm_welcome, text='Sign in', font=('josefin sans medium', 20), command=signin,
                              corner_radius=10, width=200, height=50, bg_color=('#C7EAFC', '#011E33'))
    lgn_button.place(relx=0.65, rely=0.3, anchor='center')

    new_user_label = ct.CTkLabel(frm_welcome,
                                 text='--------------------------------------------------------------\n New User?',
                                 font=('josefin sans light', 15), bg_color=('#C7EAFC', '#011E33'))
    new_user_label.place(relx=0.65, rely=0.5, anchor='center')

    sgn_button = ct.CTkButton(frm_welcome, text='Sign Up Now!', font=('josefin sans medium', 20), corner_radius=10,
                              width=200, height=50, command=signup, bg_color=('#C7EAFC', '#011E33'))
    sgn_button.place(relx=0.65, rely=0.7, anchor='center')

    switch_mode = ct.CTkSwitch(frm_welcome, text="Switch Mode", progress_color='#123456', command=sw_com,
                               fg_color='#123456', bg_color=('#C7EAFC', '#011E33'), text_color=('#011E33', '#C7EAFC'))
    switch_mode.place(relx=0.9, rely=0.95, anchor='center')

    ieee = ct.CTkLabel(frm_welcome, text=" ", image=ieee_image, bg_color=('#C7EAFC', '#011E33'))
    ieee.place(relx=0.76, rely=0.91)

    app.mainloop()


if __name__ == "__main__":
    with open("data.json", "r") as Data:
        d = json.load(Data)
    app = ct.CTk()
    app.geometry('702x500')
    app.resizable(False, False)
    ct.set_appearance_mode('dark')
    app.title('OAAA - Face Recognition Project')
    app.iconbitmap('Materials\Logo-dark.ico')
    background = ct.CTkImage(dark_image=Image.open('Materials\Background_dark.png'),
                             light_image=Image.open('Materials\Background_light.png'), size=(702, 502))
    mode = 'dark'
    email_1 = ''
    first_1 = ''
    last_1 = ''
    name = ''

    logo = ct.CTkImage(dark_image=Image.open('Materials\Logo-dark.png'),
                       light_image=Image.open('Materials\Logo-light.png'), size=(135, 135))

    ieee_image = ct.CTkImage(light_image=Image.open("Materials\ieeelogo-light.png"),
                             dark_image=Image.open('Materials\ieeelogo-dark.png'),
                             size=(30, 30))
    welcome()
