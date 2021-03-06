from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# Login and sign up screen.
class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

Builder.load_string('''
<LoginScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: (1, 1, 1, 1)
        #size_hint:root.height,root.width

    MDBoxLayout:
        orientation: 'vertical'

        MDToolbar:
            md_bg_color: app.theme_cls.bg_light
            left_action_items: [["arrow-left", lambda x: app.go_back(x, 'start-screen')]]
            specific_text_color: (0,0,0,1)

        H4:
            text: "    Login"
            size_hint: None, None
            width: root.width
            height: root.height * 0.26
            pos_hint: {'center_y': 0.5}

        MDTextField:
            id: email_textfield
            hint_text: "Email Address"
            helper_text_mode: "on_focus"
            color_mode: 'custom'
            line_color_focus: 0, 0, 0, 1
            line_color_normal: 0, 0, 0, 1
            valign: 'top'
            pos_hint: {'center_x': 0.5}
            size_hint: None, None
            height: dp(20)
            width: dp(275)
            line_color: 0.73, 0.49, 0.28, 1
            right_action_items: [["arrow-left", lambda x: app.go_back(x, 'what-are-your-goals')]]
            specific_text_color: (0,0,0,1)
            font_name: 'assets/fonts/Sofia-Pro-Light.ttf'

        MDTextField:
            id: password_textfield
            hint_text: "Password"
            helper_text_mode: "on_focus"
            color_mode: 'custom'
            line_color_focus: 0, 0, 0, 1
            line_color_normal: 0, 0, 0, 1
            valign: 'top'
            pos_hint: {'center_x': 0.5}
            size_hint: None, None
            height: dp(20)
            width: dp(275)
            line_color: 0.73, 0.49, 0.28, 1
            right_action_items: [["arrow-left", lambda x: app.go_back(x, 'what-are-your-goals')]]
            specific_text_color: (0,0,0,1)
            font_name: 'assets/fonts/Sofia-Pro-Light.ttf'

        MDBoxLayout:
            orientation: 'vertical'
            #size_hint: 1.0, 0.5
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            spacing: 20

            MDFillRoundFlatButton:
                text: "Login"
                text_color: 1, 1, 1, 1
                md_bg_color: 0.73, 0.49, 0.28, 1
                font_size: "18sp"
                size_hint: None, None
                width: root.width * 0.8
                pos_hint: {'center_x': 0.5, 'center_y': 0.25}
                font_name: 'assets/fonts/Sofia-Pro-Medium.ttf'
                line_color: 0.73, 0.49, 0.28, 1
                on_release: app.go_to(self, 'home')

            MDTextButton:
                text: "Forgot your password?"
                color: (0, 0, 0, 1)
                valign: 'center'
                pos_hint: {'center_x': 0.5}
                size_hint: None,None
                font_size: "12sp"
                font_name: 'assets/fonts/Sofia-Pro-Light.ttf'

        MDBottomAppBar:

''')