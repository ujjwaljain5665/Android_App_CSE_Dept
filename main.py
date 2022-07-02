from tkinter import dialog
from kivy.lang import Builder
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton
from kivy.uix.dropdown import DropDown
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import webbrowser
from kivymd.app import MDApp
from matplotlib.pyplot import title

KV = '''
<ContentNavigationDrawer>:
    BoxLayout:
        orientation: "vertical"
        padding: "8dp"
        spacing: "8dp"
    
        AnchorLayout:
            anchor_x: "center"
            size_hint_y: None
            height: avatar.height
    
            Image:
                id: avatar
                size_hint: None, None
                size: "100dp", "100dp"
                source: "logo.jpg"
    
        MDLabel:
            text: "Computer Science And Engineering"
            font_style: "Button"
            size_hint_y: None
            height: self.texture_size[1]
    
        MDLabel:
            text: "csedept@gehu.ac.in"
            font_style: "Caption"
            size_hint_y: None
            height: self.texture_size[1]
    
        ScrollView:
    
            MDList:
                md_bg_color: app.theme_cls.accent_color
                OneLineListItem:
                    font_style: "Button"
                    text: "HOME"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 1"
    
                OneLineListItem:
                    font_style: "Button"
                    text: "UPDATES"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 2"
                        
                OneLineListItem:
                    font_style: "Button"
                    text: "GALLERY"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 3"
    
                OneLineListItem:
                    font_style: "Button"
                    text: "COURSES"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 4"
                        
                OneLineListItem:
                    font_style: "Button"
                    text: "FACULTY"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 5"
    
                OneLineListItem:
                    font_style: "Button"
                    text: "FACILITIES"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 6"
                        
                OneLineListItem:
                    font_style: "Button"
                    text: "ABOUT US"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 7"
    
                OneLineListItem:
                    font_style: "Button"
                    text: "HELP"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 8"
                    
                    
            


Screen:
    FloatLayout:
        BoxLayout:
            MDToolbar:
                id: toolbar
                pos_hint: {'center_x': 0.5, 'top':1.0}
                elevation: 10
                title: "    CSE DEPARTMENT GEHU"
                md_bg_color: app.theme_cls.accent_color
                left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["clock", lambda x: app.callback_2()]]
        
        ScreenManager:

            id: screen_manager
            Screen:
                name: "scr 1"
                
                FloatLayout:
                    BoxLayout:
                        pos_hint: {'center_x': 0.5, 'top':0.89}
                        canvas.before:
                            Color:
                                rgba:(0,0,0,1)
                            Rectangle:
                                pos:self.pos
                                size:self.size
                        Image:
                            source:"home.gif"
                            mipmap:True
                            keep_data:True
                            anim_loop:0
                            anim_delay:0.1
                        
                    
            Screen:
                name: "scr 2"

                FloatLayout:
                    Label:
                        text:"Notice And Updates"
                        color: 0,0,0,1
                        pos_hint: {'center_x': 0.5, 'top':1.35}
                        bold: True
                        font_size: 44
			            font_name: "Comic"
                    ScrollView:
                        do_scroll: False, True
                        pos_hint: {'center_x': 0.5, 'top':.79}
                        size_hint:1,None
                        height: root.height - toolbar.height - 100
                        MDGridLayout:
                            cols: 3
                            row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                            row_force_default: True
                            adaptive_height: True
                            padding: dp(4), dp(4)
                            spacing: dp(4)
                            Button:
                                text: "Notice Regarding Fee Deposit and Registration for III Semester"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/may/Regarding-Fee-Deposit-and-Registration-for-III-Semester.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding Extension of Date for Depositing of Academic fee for the Odd Semester (V VII and IX) 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/may/Notice-Regarding-Extension-of-Date-for-Depositing-of-Academic-fee-for-the-Odd-Semester-(V-VII-and-IX)-2022.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding Filling of Back Paper Forms for Even End Semester \\nExamination 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/april/notice-Online-Back-Paper-Forms-for-Even-End-Semester-Examination.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding Odd Semester Debarred Registration and Debarred Back Paper Forms (only for final year Students)"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/april/Notice-regarding-Odd-Semester-Debarred-Registration-and-Debarred-Back-Paper-Forms-(only-for-final-year-Students).pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding Dress Code for Students 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/april/Notice-Regarding-Dress-Code-for-Students.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding Fee Deposit Odd Semester( V, VII & IX) 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/april/Notice-regarding-Fee-Deposit-for-Odd-Sem-V-&-VII-2022-23.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding filling of Online Back Paper Forms for Odd End Semester Examination April"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/april/Notice-regarding-filling-of-online-Back-Paper-Forms-for-Odd-End-Semester-Examination-April.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding Even Semester Debarred Registration & Debarred Back Paper Forms"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/april/Notice-even-sem-debarred-registration-&-debarred-back-paper-forms.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding Extension of Date for Even Mid Semester Back Paper Examinations 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/march/Notice-Regarding-Extension-of-Date-for-Even-Mid-Semester-Back-Paper-Examinations.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding Filling of Online Back Paper Examination Forms for Even Mid Semester Examination 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/march/Notice-no-72-Regarding-Filling-of-Online-Back-Paper-Forms-for-Even-Mid-Semester-Examination.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice regarding PhD Online Entrance Exam Result Full Time and Part Time 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/feb/Phd-Jan-2022-selected-candidates-(full-time).pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding End Semester PhD Exam 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/jan/Notice-Regarding-End-Sem-Exam-of-PhD-Program-(July-2021-Batch).pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding PhD Viva Voce Exam 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/jan/notice-research-exam.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding PhD Entrance Exam 2022"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/jan/revised-date-for-phd-entrance-exam.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()
                            Button:
                                text: "Notice Regarding Online Classes for III Semester 2021"
                                text_size:self.width,None
                                text_color: 0, 1, 0, 1
                                on_release:
                                    import urllib.request
                                    response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/notice/2022/jan/Regarding-online-classes-for-3rd-Sem-students.pdf')
                                    file = open("Notice" + ".pdf", 'wb')
                                    file.write(response.read())
                                    file.close()
                                    on_release:app.show()

            Screen:
                name: "scr 3"
                FloatLayout:
                    Label:
                        text:"Gallery"
                        color: 0,0,0,1
                        pos_hint: {'center_x': 0.5, 'top':1.35}
                        bold: True
                        font_size: 44
			            font_name: "Comic"
                    ScrollView:
                        canvas.before:
                            Color:
                                rgba:(0,0,0,1)
                            Rectangle:
                                pos:self.pos
                                size:self.size
                        id: scroller1
                        do_scroll: False, True
                        pos_hint: {'center_x': 0.5, 'top':.79}
                        size_hint:1,None
                        height: root.height - toolbar.height - 100
                        GridLayout:
                            rows: 5
                            cols: 1
                            pos_hint: {'center_x': 0.5, 'top':70}
                            padding: 20
                            spacing: 5,5
                            size_hint: 1, None
                            height: self.minimum_height
                            ScrollView:
                                do_scroll: True, False
                                size_hint: 1, None
                                height: 150
                                BoxLayout:
                                    orientation: 'horizontal'
                                    id: buttons_in_scrollview1
                                    size_hint: 2.0, 1.0
                                    SmartTileWithLabel:
                                        source: "logo.jpg"
                                        text: "[size=26]Graphic Era[/size]\\n[size=14]Transforming Dreams into reality[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "home.jpg"
                                        text: "[size=26]Main Building[/size]\\n[size=14]GEHU-Dehradun[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "campus.jpg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "campu.png"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "camp.jpeg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "cam.jpeg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "auditorium.jpg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                        
                            ScrollView:
                                do_scroll: True, False
                                size_hint: 1, None
                                height: 150
                                BoxLayout:
                                    orientation: 'horizontal'
                                    id: buttons_in_scrollview2
                                    size_hint: 2.0, 1.0
                                    SmartTileWithLabel:
                                        source: "grafest.jpg"
                                        text: "[size=26]Graphic Era[/size]\\n[size=14]Transforming Dreams into reality[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "Grafest-07.jpg"
                                        text: "[size=26]Main Building[/size]\\n[size=14]GEHU-Dehradun[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "images (1).jpg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "chetan.jpg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "images.jpg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "urvashi.png"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                            ScrollView:
                                do_scroll: True, False
                                size_hint: 1, None
                                height: 150
                                BoxLayout:
                                    orientation: 'horizontal'
                                    id: buttons_in_scrollview3
                                    size_hint: 2.0, 1.0
                                    SmartTileWithLabel:
                                        source: "img1.jpg"
                                        text: "[size=26]Foundation Day[/size]\\n[size=14]GEHU[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "img.jpg"
                                        text: "[size=26]Foundation Day[/size]\\n[size=14]GEHU[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "ch.jpeg"
                                        text: "[size=26]Foundation Day[/size]\\n[size=14]GEHU[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "fd.jpg"
                                        text: "[size=26]Foundation Day[/size]\\n[size=14]GEHU[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "fd1.jpg"
                                        text: "[size=26]Foundation Day[/size]\\n[size=14]GEHU[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "fd2.jpg"
                                        text: "[size=26]Foundation Day[/size]\\n[size=14]GEHU[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "fd3.jpg"
                                        text: "[size=26]Foundation Day[/size]\\n[size=14]GEHU[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                            ScrollView:
                                do_scroll: True, False
                                size_hint: 1, None
                                height: 150
                                BoxLayout:
                                    orientation: 'horizontal'
                                    id: buttons_in_scrollview2
                                    size_hint: 2.0, 1.0
                                    SmartTileWithLabel:
                                        source: "Kamal.jpg"
                                        text: "[size=26]Chancellor[/size]\\n[size=14]Prof.(Dr) Kamal Ghanshala[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "snajay.png"
                                        text: "[size=26]Vice-Chancellor[/size]\\n[size=14]Prof.(Dr) Sanjay Jasola[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "sj1.jpg"
                                        text: "[size=26]Chancellor[/size]\\n[size=14]Prof.(Dr) Kamal Ghanshala[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "int.jpg"
                                        text: "[size=26]Internation Interaction[/size]\\n[size=14][/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "int1.jpg"
                                        text: "[size=26]Internation Interaction[/size]\\n[size=14][/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "sj.jpg"
                                        text: "[size=26]Silver Jubilee[/size]\\n[size=14]Graphic Era[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                            ScrollView:
                                do_scroll: True, False
                                size_hint: 1, None
                                height: 150
                                BoxLayout:
                                    orientation: 'horizontal'
                                    id: buttons_in_scrollview2
                                    size_hint: 2.0, 1.0
                                    SmartTileWithLabel:
                                        source: "grafest.jpg"
                                        text: "[size=26]Graphic Era[/size]\\n[size=14]Transforming Dreams into reality[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "Grafest-07.jpg"
                                        text: "[size=26]Main Building[/size]\\n[size=14]GEHU-Dehradun[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "images (1).jpg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "chetan.jpg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "images.jpg"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                    SmartTileWithLabel:
                                        source: "urvashi.png"
                                        text: "[size=26]GEHU[/size]\\n[size=14]Campus[/size]"
                                        tile_text_color: app.theme_cls.accent_color
                                        
            Screen:
                name: "scr 4"
                FloatLayout:
                    Label:
                        text:"Courses Offered"
                        color: 0,0,0,1
                        pos_hint: {'center_x': 0.5, 'top':1.35}
                        bold: True
                        font_size: 44
			            font_name: "Comic"
                    ScrollView:
                        id: scroller2
                        do_scroll: False, True
                        pos_hint: {'center_x': 0.5, 'top':.79}
                        size_hint:1,None
                        height: root.height - toolbar.height - 100
                        MDGridLayout:
                            cols: 1
                            adaptive_height: True
                            padding: dp(4), dp(4)
                            spacing: dp(4)
                            
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"B.TECH COMPUTER SCIENCE AND ENGINEERING:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-The B. Tech in Computer Science and Engineering aims to develop graduates that are not only well versed with traditional computing approaches but are also experienced in modern tools, technologies, and diverse applications.\\nThe program has a comprehensive set of fundamental courses in computer science and many electives. This enables the students to build a program most suitable for them.\\n-The program will prepare students to work in the IT industry as well as in the research areas like computer vision, machine learning, image processing, pattern recognition, virtual/augmented reality, etc.\\n-The program will also provide current research trends for students, who want to pursue higher studies, to take up higher studies in CS.\\n\\nCareer Prospects: Software Engineer, System Analyst, Software Developer, System Scientist, System Engineer etc.\\nEligibility:10+2 (PCM)\\nAdmission Procedure:Merit prepared on basis of (10+2)% / JEE Main Score\\n"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 3
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                MDRoundFlatButton:
                                    text: "Fees"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/fee/b.tech-cse-fee-structure.pdf')
                                        file = open("Fees" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Curriculum"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/curriculum/btech%20cse%20curriculum.pdf')
                                        file = open("Curriculum" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Apply"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import webbrowser
                                        webbrowser.open('https://www.gehu.ac.in/content/gehu/en/admission-form.html')
                            
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nB.TECH COMPUTER SCIENCE & ENGINEERING (HONS.) WITH SPECIALIZATION IN ARTIFICIAL INTELLIGENCE & MACHINE LEARNING:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-Machine learning is the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome.\\n-Machine learning is so pervasive today that it is probably used dozens of times a day without knowing it by the people. Many researchers also think it is the best way to make progress towards human-level AI.\\n-In this program, The Students will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for society. More importantly, Students will learn about not only the theoretical underpinnings of learning but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Course content shall be delivered by industry persons from IBM.\\n\\nCareer Prospects: Data Scientist, Machine Learning Scientist, Lead Machine Learning Researcher, Machine Learning Algorithm Developer, Video ML Engineer etc.\\nEligibility:10+2 (PCM)\\nAdmission Procedure:Merit prepared on basis of (10+2)% / JEE Main Score\\n"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 3
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                MDRoundFlatButton:
                                    text: "Fees"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/fee/b.tech-cst-fee-structure.pdf')
                                        file = open("Fees" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Curriculum"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/curriculum/B.Tech-CS&T-Machine-Learning-AI-Curriculum.pdf')
                                        file = open("Curriculum" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Apply"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import webbrowser
                                        webbrowser.open('https://www.gehu.ac.in/content/gehu/en/admission-form.html')
                            
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nB.TECH COMPUTER SCIENCE & ENGINEERING (HONS.) WITH SPECIALIZATION IN CLOUD COMPUTING:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-Cloud Computing is one of the fastest growing concepts in the IT industry today and being increasingly adopted by most of the business organizations to get out of the complexity of managing data centers and IT infrastructure.\\n-B. Tech program in Cloud Computing teaches the students about cloud phenomenon and all the related technologies, Virtualization technology, which is the core technology on which the cloud-computing paradigm works; hence, its study scope is based on latest methodologies, models, and security trends. Besides teaching about the history of the cloud and its roots in Service Oriented Architecture, DevOps and Utility Security in Cloud Computing, it also gives an introduction to Open Source Software and Open Standards. Course content shall be delivered by industry persons from IBM\\n\\nCareer Prospects: Cloud Solution Architects, Cloud System Administrator, Cloud Security Specialists, Cloud Application Development/Maintenance/Testing, Migration & Modernization Specialists and Cloud Project Managers.\\nEligibility:10+2 (PCM)\\nAdmission Procedure:Merit prepared on basis of (10+2)% / JEE Main Score\\n"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 3
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                MDRoundFlatButton:
                                    text: "Fees"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/fee/b.tech-cst-fee-structure.pdf')
                                        file = open("Fees" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Curriculum"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/curriculum/B.Tech-CS&T-Cloud-Computing-Curriculum.pdf')
                                        file = open("Curriculum" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Apply"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import webbrowser
                                        webbrowser.open('https://www.gehu.ac.in/content/gehu/en/admission-form.html')
                                    
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nB.TECH COMPUTER SCIENCE & ENGINEERING (HONS.) WITH SPECIALIZATION IN CYBER SECURITY:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-Information security often referred to as InfoSec, refers to the processes and tools designed and deployed to protect sensitive business information from modification, disruption, destruction, and inspection.\\n-Information security and cybersecurity are often confused. InfoSec is a crucial part of cybersecurity, but it refers exclusively to the processes designed for data security.\\n-The B. Tech in CE (Hons) with specialization in Information Security offered at Graphic Era aims to develop graduates that are not only well versed with traditional computing approaches but are also experienced in modern tools, specialized technologies, and diverse applications relating to the field of Information Security\\n-The rapid rise in cyber-terrorism, misuse of social media and internet usage, technology security experts think there shall be a growing demand for graduates with specialized knowledge of Information security.\\n\\nCareer Prospects:\\n-Graduates shall have a plethora of opportunities in the job market and can work for a number of organizations both government and private, both in India and abroad.\\n-Positions may include Cyber Forensics Solutions architect, malware analyst, Intelligence analyst, Information Security Analyst, Expert at Antivirus firms, Computer, and Information system manager, or network security analyst.\\nEligibility:10+2 (PCM)\\nAdmission Procedure:Merit prepared on basis of (10+2)% / JEE Main Score\\n"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 3
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                MDRoundFlatButton:
                                    text: "Fees"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/fee/b.tech-ce-fee-structure.pdf')
                                        file = open("Fees" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Curriculum"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/curriculum/B.Tech-CE-Cyber-Security-Curriculum.pdf')
                                        file = open("Curriculum" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Apply"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import webbrowser
                                        webbrowser.open('https://www.gehu.ac.in/content/gehu/en/admission-form.html')
                                    
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nB.TECH COMPUTER SCIENCE & ENGINEERING (HONS.) WITH SPECIALIZATION IN BLOCKCHAIN:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-The B.Tech in CE (Hons) with specialisation in Blockchain program at Graphic Era aims to develop graduates not only well versed with the foundational and advanced computing approaches but also specialised in the decentralised Blockchain technology (or popularly referred to as the Distributed Ledger Technology)\\n-This technology makes the history of any digital asset unalterable and transparent through the use of decentralization and cryptographic hashing.\\n-Applications of Blockchain can be seen in almost every industry- the ledger technology can be applied to track fraud across any domain thereby bringing scaleability of trust via technology.\\n-Blockchain technology has attracted many organisations who want to add transparency of transactions to their security structures.\\n\\nCareer Prospects: The application of Blockchain technology is not limited only to the finance industry: it’s growing importance in different sectors such as supply chain management, digital advertising, forecasting, cybersecurity, Internet of things, networking, etc. can already be felt. Blockchain technology also has a huge prospective to provide new openings for occupation in the industry. It also enhances the professional’s capability to upgrade themselves. Blockchain technology applications may also be found in government systems as they make their operations much more secure and efficient.\\nEligibility:10+2 (PCM)\\nAdmission Procedure:Merit prepared on basis of (10+2)% / JEE Main Score\\n"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 3
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                MDRoundFlatButton:
                                    text: "Fees"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/fee/b.tech-ce-fee-structure.pdf')
                                        file = open("Fees" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Curriculum"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/curriculum/B.Tech-CE-Blockchain-Curriculum.pdf')
                                        file = open("Curriculum" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Apply"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import webbrowser
                                        webbrowser.open('https://www.gehu.ac.in/content/gehu/en/admission-form.html')
                                    
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nB.TECH COMPUTER SCIENCE & ENGINEERING (HONS.) WITH SPECIALIZATION IN INFORMATION SECURITY AND ARTIFICIAL INTELLIGENCE:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-A BTech CE with a specialization in Information Security and Artificial Intelligence is a pathway to technical and tactical proficiency. The Department of Computer Engineering, Graphic Era Hill University, Dehradun, aims to impart quality, substantial education that allows students to play with intriguing ideas, brainstorm innovative solutions for the toughest puzzles, investigate inferences to complicated problems, and apply their learnings of mathematics, science, and engineering fundamentals in practical scenarios. Be a part of the most dynamic, evolving, and thrilling field of InfoSec and understand how to protect data like a pro with a BTech CE Information Security and Artificial Intelligence Specialization.\\nThe university provides students with opportunities to pursue multiple value-added certifications that allow them to build their skill-set with respect to future employability. The course emphasizes on the Information Security development life cycle of an organization and inculcates concepts of Artificial Intelligence so as to achieve efficient and optimal results. Learn key concepts like information architecture, data security, network security, identity management, etc. Through the course, aspirants learn how to plan and implement corporate information security policies, analyze security risks of an organization, implement various security mechanisms, and more, with automated techniques generated through Artificial Intelligence and Machine Learning.\\n\\nCareer Prospects: A BTech with Graphic Era Hill University, Dehradun, gives you the wind beneath your wings to help you explore the world. Upon graduation, students can work as chief information security officers, risk assessment specialists, security policy developers, cybersecurity specialists, risk analysts, etc.\\nEligibility:10+2 (PCM)\\nAdmission Procedure:Merit prepared on basis of (10+2)% / JEE Main Score\\n"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 2
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                MDRoundFlatButton:
                                    text: "Fees"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/fee/b.tech-computer-engineering-information-security-artificial-intelligence.pdf')
                                        file = open("Fees" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Apply"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import webbrowser
                                        webbrowser.open('https://www.gehu.ac.in/content/gehu/en/admission-form.html')
                                    
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nB.TECH COMPUTER SCIENCE & ENGINEERING (HONS.) WITH SPECIALIZATION IN ARTIFICIAL INTELLIGENCE AND ROBOT BUILDING:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-Pursuing a BTech in Computer Engineering at Graphic Era Hill University, Dehradun, is a journey of sheer illumination and revelation. The university aims at nurturing the minds of future engineers to innovate technically advanced and practical solutions to help refine the quality of lives all around the world. Get a firm grasp on technology and engineer your future with a BTech CE degree specializing in Artificial Intelligence and Robotics. With an emphasis on applications of science, mathematics, operations, and technology, a BTech CE degree specializing in Artificial Intelligence and Robotics is the first step for an aspirant towards a challenging, yet rewarding career. The course is introduced to meet the great demand for AI and Robotics engineers in various sectors like manufacturing, health, automobile, technology, and more. The incorporation of Artificial Intelligence in Robotics allows for greater customization, efficiency, and flexibility in otherwise rigid applications. \\nA BTech CE allows one to figure out practical use cases for scientific notions, and apply cutting-edge techniques and technologies to build, design, maintain and operate complex systems and processes. The specialization in AI and Robotics helps enable students to build intelligent machines, software, or applications with an innovative implementation of machine learning and visualization technologies. Through this program, students will be equipped with a strong foundation in subjects like Intelligent Systems, applying AI for games, Machine Learning, Data Visualization, etc.\\n\\nCareer Prospects: The employment opportunities in the world of Computer Engineering are vast and endless. Graduates of this course gain a sound knowledge of Advanced Signal Processing Techniques and practical application of various programming languages. A few job profiles an aspirant of an AI and Robotics engineer can work under are Machine Learning Engineer, Robotics Scientist, AI Research Scientist, Data Scientist, Business Intelligence Developer, etc.\\nEligibility:10+2 (PCM)\\nAdmission Procedure:Merit prepared on basis of (10+2)% / JEE Main Score\\n"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 2
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                MDRoundFlatButton:
                                    text: "Fees"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/fee/b.tech-computer%20engineering-artificial-intelligence-robot-building.pdf')
                                        file = open("Fees" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Apply"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import webbrowser
                                        webbrowser.open('https://www.gehu.ac.in/content/gehu/en/admission-form.html')
                                    
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nB.TECH COMPUTER SCIENCE & ENGINEERING (HONS.) WITH SPECIALIZATION IN DEEP LEARNING & ARTIFICIAL INTELLIGENCE:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-Pursuing a BTech in Computer Engineering at Graphic Era Hill University, Dehradun, is a journey of sheer illumination and revelation, and is an opportunity to transform and revamp educative experiences for all aspirants. The department of Computer Engineering strives to nurture acumen, creativity, and intellect amongst all, throughout their journey from a student to becoming a skillful engineer. Deep learning is a subset of machine learning where a large amount of data enables the learning of artificial neural networks through various algorithms. Deep Learning and Artificial Intelligence enable machines to do intelligence tasks with acquired skills and experience.\\nInnovate, inspire, and excel with a BTech in Computer Engineering Deep Learning and Artificial Intelligence specialization from Graphic Era Hill University. Strengthen your understanding of subjects like Reinforcement Learning, Neural Networks, Deep Learning, TensorFlow, Random Forest, and Boosting. The course equips aspirants to gain a practical understanding of Deep Learning in Artificial Intelligence and Machine Learning functions and develop a strong foundation in programming and statistics.\\n\\nCareer Prospects: The employment opportunities in the world of Computer Engineering are vast and endless. With a degree as resourceful and prominent as BTech CE specializing in Deep Learning and Artificial Intelligence, a student can venture into any domain of industry they aspire to be a significant part of. Graduates can work in leading organizations as Researchers, Scientists, Analysts, Software Engineers, Game Developers, System Engineers, and Network Engineers.\\nEligibility:10+2 (PCM)\\nAdmission Procedure:Merit prepared on basis of (10+2)% / JEE Main Score\\n"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 2
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                MDRoundFlatButton:
                                    text: "Fees"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/fee/btech-computer-engineering-deep-learning-artificial-intelligence.pdf')
                                        file = open("Fees" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Apply"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import webbrowser
                                        webbrowser.open('https://www.gehu.ac.in/content/gehu/en/admission-form.html')
                                    
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nINTEGRATED PROGRAMMES:\\nB.TECH COMPUTER SCIENCE & ENGINEERING:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-Eligibility:10th\\nAdmission Procedure:Merit prepared on basis of 10th\\nDuration:6 Years\\n"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 2
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                MDRoundFlatButton:
                                    text: "Fees"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import urllib.request
                                        response = urllib.request.urlopen('https://www.gehu.ac.in/content/dam/gehu/pdf/course/ug/soe/fee/Integrated-Btech-CS-6-Year.pdf')
                                        file = open("Fees" + ".pdf", 'wb')
                                        file.write(response.read())
                                        file.close()
                                        on_release:app.show()
                                MDRoundFlatButton:
                                    text: "Apply"
                                    text_color: 0, 1, 0, 1
                                    on_release:
                                        import webbrowser
                                        webbrowser.open('https://www.gehu.ac.in/content/gehu/en/admission-form.html')
                                    
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nDOCTORAL PROGRAMMES:\\nP.HD IN COMPUTER SCIENCE & ENGINEERING:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDLabel:
                                size_hint_y: None
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"\\nProgram Details:\\n\\n-Eligibility:Master’s Degree from any AIU/UGC/AICTE recognized University/ Institutions or any other qualification recognized as equivalent thereto in the fields of study notified from time to time by the University. A minimum of 55% marks or CGPA of 5.5 on a 10 point scale in the qualifying examination (50% marks or CGPA of 5.0 on a 10 point scale for SC/ST candidates).\\nAdmission Procedure:Admissions are on the basis of GATE/NET/SLET scores or written test followed by an interview by the Department concerned with due attention to National/State Reservation.\\n\\nContact person for PhD. Admissions:Dr. Vivek Jaglan\\nEmail: phd@gehu.ac.in"
                                bold:True
                                font_size: 20
			                    font_name: "Arial"
                            
                    
            Screen:
                name: "scr 5"
                    
                FloatLayout:
                    Label:
                        text:"Faculty"
                        color: 0,0,0,1
                        pos_hint: {'center_x': 0.5, 'top':1.35}
                        bold: True
                        font_size: 44
			            font_name: "Comic"
                    ScrollView:
                        id: scroller2
                        do_scroll: False, True
                        pos_hint: {'center_x': 0.5, 'top':.79}
                        size_hint:1,None
                        height: root.height - toolbar.height - 100
                        MDGridLayout:
                            cols: 3
                            row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                            row_force_default: True
                            adaptive_height: True
                            padding: dp(4), dp(4)
                            spacing: dp(4)
                            SmartTileWithLabel:
                                source: "Dr. Mahantesh Pattanshetti.jpg"
                                text: "[size=26]Dr. Mahantesh Pattanshetti[/size]\\n[size=14]Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Ashok Sahoo.jpg"
                                text: "[size=26]Mr. Ashok Sahoo[/size]\\n[size=14]Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Dr. Mahesh Manchanda.jpg"
                                text: "[size=26][color=#ffffff]Dr. Mahesh Manchanda[/color][/size]\\n[size=14]Associate Professor[/size]"
                                
                            
                            SmartTileWithLabel:
                                source: "Dr. Vrince Vimal .jpg"
                                text: "[size=26]Dr. Vrince Vimal[/size]\\n[size=14]Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "prof-Bhagavant-k-Deshpande.jpg"
                                text: "[size=26]Prof. (Dr.)Bhagavant.k.Deshpande[/size]\\n[size=14]Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Navin Garg.jpg"
                                text: "[size=26][color=#ffffff]Mr. Navin Garg[/color][/size]\\n[size=14]Associate Professor[/size]"
                                
                                
                            SmartTileWithLabel:
                                source: "A.B.-Desai.jpg"
                                text: "[size=26]Mr.A.B.-Desai[/size]\\n[size=14]Associate Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Dr. Ved Prakash Dubey.jpg"
                                text: "[size=26]Dr. Ved Prakash Dubey[/size]\\n[size=14]Associate Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Kuljinder Singh Bumrah.jpg"
                                text: "[size=26][color=#ffffff]Mr. Kuljinder Singh Bumrah[/color][/size]\\n[size=14]Assistant Professor[/size]"
                                
                                
                            SmartTileWithLabel:
                                source: "Ms. Poonam Rani.jpg"
                                text: "[size=26]Ms. Poonam Rani[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Amit Mishra - CSE.jpg"
                                text: "[size=26]Mr. Amit Mishra[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Umang Garg - CA.jpg"
                                text: "[size=26][color=#ffffff]Mr. Umang Garg[/color][/size]\\n[size=14]Assistant Professor[/size]"
                                
                            
                            SmartTileWithLabel:
                                source: "Mr. Avnish Panwar - CSE.jpg"
                                text: "[size=26]Mr. Avnish Panwar[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Ms. Manika.jpg"
                                text: "[size=26]Ms. Manika[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mrs. Rishika Yadav.jpg"
                                text: "[size=26][color=#ffffff]Mrs. Rishika Yadav[/color][/size]\\n[size=14]Assistant Professor[/size]"
                                
                                
                            SmartTileWithLabel:
                                source: "Mrs. Sonali Gupta.jpg"
                                text: "[size=26]Mrs. Sonali Gupta[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mrs Manisha Aeri.jpg"
                                text: "[size=26]Mrs Manisha Aeri[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Sumeshwar Singh.jpg"
                                text: "[size=26][color=#ffffff]Mr. Sumeshwar Singh[/color][/size]\\n[size=14]Assistant Professor[/size]"
                                
                                
                            
                            SmartTileWithLabel:
                                source: "Mr. Sushant Chamoli.jpg"
                                text: "[size=26]Mr. Sushant Chamoli[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Piyush Bagla - CSE.jpg"
                                text: "[size=26]Mr. Piyush Bagla[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Sameer Rana.jpg"
                                text: "[size=26][color=#ffffff]Mr. Sameer Rana[/color][/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Dr. Akshay kumar.jpg"
                                text: "[size=26]Dr. Akshay kumar[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Dr Inderjeet.jpg"
                                text: "[size=26][color=#ffffff]Dr Inderjeet[/color][/size]\\n[size=14]Assistant Professor[/size]"
                                
                                
                            SmartTileWithLabel:
                                source: "Mrs. Preeti Chaudhary .jpg"
                                text: "[size=26]Mrs. Preeti Chaudhary[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Ms. Lisa Gopal.jpg"
                                text: "[size=26]Ms. Lisa Gopal[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Ms. Ayushi.jpg"
                                text: "[size=26][color=#ffffff]Ms. Ayushi[/color][/size]\\n[size=14]Assistant Professor[/size]"
                                
                                
                            SmartTileWithLabel:
                                source: "Ms. Aditya.jpg"
                                text: "[size=26]Ms. Aditya[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Saumitra Chattopadhyay.jpg"
                                text: "[size=26]Mr. Saumitra Chattopadhyay[/size]\\n[size=14]Assistant Professor[/size]"
                                
    
                            SmartTileWithLabel:
                                source: "Mr. Chetan Pandey.jpg"
                                text: "[size=26][color=#ffffff]Mr. Chetan Pandey[/color][/size]\\n[size=14]Assistant Professor[/size]"
                                
                                
                         
            Screen:
                name: "scr 6"
                FloatLayout:
                    Label:
                        id:headingf
                        text:"Facilities : "
                        color: 0,0,0,1
                        pos_hint: {'center_x': 0.18, 'top':1.33}
                        bold: True
                        font_size: 44
			            font_name: "Arial"
                    ScrollView:
                        do_scroll_x: False
                        do_scroll_y: True
                        pos_hint: {'center_x': 0.5, 'top':0.75}
                        size_hint: 1, None
                        height: root.height - toolbar.height - 100
                        MDGridLayout:
                            cols: 1
                            adaptive_height: True
                            padding: dp(4), dp(4)
                            spacing: dp(4)
                            MDLabel:
                                size_hint_y: None
                                md_bg_color:0,0,0,0.5
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text: "Technology is evolving at a very fast pace. The prime aim of the department is to get its students aligned with the same. The department's continuous efforts are to equip the students with latest technical skills to cope up with the trends and the needs of the industry. Keeping this view in mind, the Computer Science and Engineering department focuses more and more on project and lab based learning, seminars and webinars. To bolster this effort sophisticated and State-of-Art labs equipped with latest equipments (hardware and software) are being used. This not only imparts high class theoretical knowledge but also trains the students with real time practical scenarios, facilitating the transition of the students from academics to the industry.\\n\\nThe Ubuntu lab epitomizes elegance and adeptness. Elegance in terms of design and adeptness in terms of smart 200 plus computer systems that can cater to most of the demands of resource hungry softwares. The CISCO is designed with in collaboration with CISCO Systems. It is a fully equipped networking academy in itself. The students accumulate skills from the likes of basic work such as crimping to creating advanced and complex networks. The IOT lab provides the students with all the resources needed for creating working models in the space of Internet of Things."
                                font_size: 24
			                    font_name: "Comic"
                            MDLabel:
                                size_hint_y: None
                                md_bg_color:1,1,1,1
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"CISCO NETWORKING ACADEMY:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 3
                                md_bg_color:0,0,0,1
                                row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                                row_force_default: True
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                Image:
                                    source:"c1.jpg"
                                Image:
                                    source:"c2.jpg"
                                Image:
                                    source:"c3.jpg"
                            MDLabel:
                                size_hint_y: None
                                md_bg_color:1,1,1,1
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"INTERNET OF THINGS LAB:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 3
                                md_bg_color:0,0,0,1
                                row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                                row_force_default: True
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                Image:
                                    source:"i1.jpg"
                                Image:
                                    source:"i2.jpg"
                                Image:
                                    source:"i3.jpg"
                            MDLabel:
                                size_hint_y: None
                                md_bg_color:1,1,1,1
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"UBUNTU COMPUTER CENTER:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 3
                                md_bg_color:0,0,0,1
                                row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                                row_force_default: True
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                Image:
                                    source:"u1.jpg"
                                Image:
                                    source:"u2.jpg"
                                Image:
                                    source:"u3.jpg"
                            MDLabel:
                                size_hint_y: None
                                md_bg_color:1,1,1,1
                                height: self.texture_size[1]
                                text_size: self.width, None
                                color: 0,0,0,1
                                text:"MAC COMPUTER CENTER:"
                                bold:True
                                font_size: 24
			                    font_name: "Arial"
                            MDGridLayout:
                                cols: 3
                                md_bg_color:0,0,0,1
                                row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                                row_force_default: True
                                adaptive_height: True
                                padding: dp(4), dp(4)
                                spacing: dp(4)
                                Image:
                                    source:"m1.jpg"
                                Image:
                                    source:"m2.jpg"
                                Image:
                                    source:"m3.jpg"
                            
                   

            Screen:
                name: "scr 7"
                
                FloatLayout:
                    Label:
                        id:heading
                        text:"Graphic Era Hill University Dehradun"
                        color: 0,0,0,1
                        pos_hint: {'center_x': 0.5, 'top':1.35}
                        bold: True
                        font_size: 44
			            font_name: "Comic"
                    FitImage:
                        id: homeimg
                        pos_hint: {'center_x': 0.5, 'top':0.79}
                        size_hint: 0.55, 0.50
                        allow_stretch: True
                        source: "home.jpg"
                    ScrollView:
                        do_scroll_x: False
                        do_scroll_y: True
                        pos_hint: {'center_x': 0.5, 'top':0.25}
                        size_hint: 1, None
                        height: root.height - homeimg.height - toolbar.height - 100
                        MDLabel:
                            size_hint_y: None
                            md_bg_color:0,0,0,0.5
                            height: self.texture_size[1]
                            text_size: self.width, None
                            padding: 40, 0
                            color: 0.5,0.9,0.1,1
                            text: "Established vide Act No 12 of 2011 of Uttarakhand State Legislature.University under Section 2(f) of the UGC Act, 1956 set up under the aegis of Graphic Era Educational Society, Dehradun. Founded in 2011 Graphic Era Hill University is today widely known for its innovative and rigorous education which has nurtured professionals across industries and sectors in India and beyond. Graphic Era Hill University has adopted a global approach to education and research with focus on International perspectives and expertise. University has abiding commitment to excellence and pursues this relentlessly settling for nothing, but the best. Its faculty is the bedrock of the University and composed of academic luminaries across India and abroad. GEHU is on the cutting edge of using state-of-the art equipment and preparing students for globalized economy and at the same time promoting holistic learning, unbiased knowledge ,industry centric skills, ethics, a cosmopolitan outlook and accountability for actions. GEHU is making its presence at national and international platforms, through collaborations with premier universities of the world, study abroad programs and international internships and research.Graphic Era Hill University offers comprehensive curriculum over a large number of degree programs in engineering, law, management, computer applications, humanities, applied sciences, animation, fashion designing, journalism and mass communication, Agriculture. These programs offer the students multiple academic pathways. The University has an abiding commitment to create excellent education opportunities for the youth hailing from the hills, at affordable cost. Therefore 25% concession in the fee is offered to the students of hill areas, across the country. University also offers unstinting support for community services, through its social responsibility endeavors.\\n\\n About the Computer Science and Engineering Department:\\n\\n The Department of Computer Science and Engineering at GEHU aspires to equip its students with the latest technical skills in order to cope well with the trends and the needs of the industry. Our academic curricula is tailored and designed to cater to the requirements of industrial deployment and research activities. Besides the rigorous academic schedule, heavy focus is laid on online courses like MOOC that enable the students to become part of various premiere universities in the world. To encourage research and development among students, sophisticated and State-of-Art labs equipped with latest equipments (hardware and software) are being used hence making them au fait with the latest technical game. By legally collaborating with the industry giants like Sapient Razorfish we make sure that our students are well placed all over in various multinationals. More and more focus is being given to project and lab based learning, seminars, webinars, guest lectures, conferences and regular visits by various industry experts. This not only imparts high class theoretical knowledge but also trains the students with practical scenarios hence facilitating the transition of the students from academics to the industry.\\nOur aim is to complement students’ formal education with strong technical know-how in emerging technologies in various engineering sectors of the industry thereby helping in the overall development of their personalities as astute professionals.\\n\\nVision:\\n\\nTo become a center of excellence in the Computer science and engineering discipline with a strong research and teaching environment that adapts swiftly to the challenges of the 21st century.\\n\\nMission:\\n\\nM1) To provide qualitative education and generate new knowledge by engaging in cutting-edge research and by offering state-of-the-art undergraduate, postgraduate and doctoral programs, leading to careers as Computer and IT professionals in the widely diversified domains of industry, government and academia.\\nM2) To promote a teaching and learning process that yields advancements in state-of-the-art in Computer Science and Information Technology, resulting in integration of research results and innovations into other scientific disciplines leading to new technologies and products.\\nM3) To harness capital for sustainable competitive edge and social relevance by inculcating the philosophy of continuous learning and innovation in Computer Science."
                            font_size: 24
                            bold:True
			                font_name: "Times"
                            

            Screen:
                name: "scr 8"
                
                FloatLayout:
                    BoxLayout:
                        orientation: 'vertical'
                        pos_hint: {'center_x': 0.5, 'top':0.89}
                        Image:
                            source:"logo.jpg"
                        Label:
                            color: 0,0,0,1
                            text:"For Any Queries Reach Out To Us At : \\n\\nCall (Operational 9AM-6PM): 18008906027, 18002701280, 7500013334\\n\\nWhatsApp: +917617770113\\n\\nEmail : cse@gehu.ac.in"
                            pos_hint: {'center_x': 0.7, 'top':0.50}
                            text_size:self.width,None
                            bold:True
			                font_name: "Arial"
                
    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer
    
'''

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CSE_GEHU(MDApp):
    dialog=None
    def build(self):
        return Builder.load_string(KV)
    def show(self):
        if not self.dialog:
            self.dialog=MDDialog(title="File Downloaded SuccesFully.",buttons=[
                MDFlatButton(text="Ok",on_release=self.close)],
                )
        self.dialog.open()
    def close(self,instance):
        self.dialog.dismiss()


CSE_GEHU().run()