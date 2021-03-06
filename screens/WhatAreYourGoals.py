from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class WhatAreYourGoals(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


Builder.load_string('''
<WhatAreYourGoals>:
    MDBoxLayout:
        orientation: 'vertical'

        MDToolbar:
            md_bg_color: app.theme_cls.bg_light
            left_action_items: [["arrow-left", lambda x: app.go_back(x, 'signup-with-email')]]
            specific_text_color: (0,0,0,1)

        H4:
            text: "    What are \\n    your goals?"
            pos_hint: {'center_y': 0.5}

        MDBoxLayout:
            orientation: 'vertical'
            spacing: 20

            WhiteAppButton:
                id: strength
                text: 'Strength'
                width: root.width * 0.8
                on_release: app.current_user.goals = 'Strength'

            WhiteAppButton:
                id: hypertrophy
                text: 'Hypertrophy'
                width: root.width * 0.8
                on_release: app.current_user.goals = 'Hypertrophy'

            WhiteAppButton:
                id: functionality
                text: 'Functionality'
                width: root.width * 0.8
                on_release: app.current_user.goals = 'Functionality'

        MDBoxLayout:
            orientation: 'vertical'
            #size_hint: 1.0, 0.5
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            spacing: 20

            AppButton:
                text: 'Continue'
                valign: 'center'
                width: root.width * 0.8
                height: dp(25)
                pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                on_release: app.go_to(self, 'what-is-your-level')

            AppTextButton:
                text: 'Skip For Now'
                valign: 'center'
                pos_hint: {'center_x': 0.5}
                size_hint: None,None

        MDBottomAppBar:
        
''')