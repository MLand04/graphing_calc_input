import math
from guizero import App, Combo, Text, TextBox, CheckBox, ButtonGroup, PushButton

def say_my_name():
        welcome_message.value = my_name.value


app = App(title="math", width=1280, height=400, layout="grid")




x_1 = PushButton(app, command=say_my_name, text="1", grid=[0,2], align="left", width=6, height=4)
x_2 = PushButton(app, command=say_my_name, text="2", grid=[1,2], align="left", width=6, height=4)
x_3 = PushButton(app, command=say_my_name, text="3", grid=[2,2], align="left", width=6, height=4)
x_4 = PushButton(app, command=say_my_name, text="4", grid=[0,3], align="left", width=6, height=4)
x_5 = PushButton(app, command=say_my_name, text="5", grid=[1,3], align="left", width=6, height=4)
x_6 = PushButton(app, command=say_my_name, text="6", grid=[2,3], align="left", width=6, height=4)
x_7 = PushButton(app, command=say_my_name, text="7", grid=[0,4], align="left", width=6, height=4)
x_8 = PushButton(app, command=say_my_name, text="8", grid=[1,4], align="left", width=6, height=4)
x_9 = PushButton(app, command=say_my_name, text="9", grid=[2,4], align="left", width=6, height=4)
x_0 = PushButton(app, command=say_my_name, text="0", grid=[3,4], align="left", width=6, height=4)
x_dot = PushButton(app, command=say_my_name, text=".", grid=[3,3], align="left", width=6, height=4)
x_negative = PushButton(app, command=say_my_name, text="(-)", grid=[3,2], align="left", width=6, height=4)
x_divide = PushButton(app, command=say_my_name, text="/", grid=[7,2], align="left", width=6, height=4)
x_multiply = PushButton(app, command=say_my_name, text="*", grid=[6,2], align="left", width=6, height=4)
x_subtract = PushButton(app, command=say_my_name, text="-", grid=[5,2], align="left", width=6, height=4)
x_plus = PushButton(app, command=say_my_name, text="+", grid=[4,2], align="left", width=6, height=4)
x_open_bracket = PushButton(app, command=say_my_name, text="(", grid=[8,2], align="left", width=6, height=4)
x_sin = PushButton(app, command=say_my_name, text="sin", grid=[4,3], align="left", width=6, height=4)
x_cos = PushButton(app, command=say_my_name, text="cos", grid=[5,3], align="left", width=6, height=4)
x_tan = PushButton(app, command=say_my_name, text="tan", grid=[6,3], align="left", width=6, height=4)
x_close_Bracket = PushButton(app, command=say_my_name, text=")", grid=[9,2], align="left", width=6, height=4)
x_arcsin = PushButton(app, command=say_my_name, text="arcsin", grid=[4,4], align="left", width=6, height=4)
x_arccos = PushButton(app, command=say_my_name, text="arccos", grid=[5,4], align="left", width=6, height=4)
x_arctan = PushButton(app, command=say_my_name, text="arctan", grid=[6,4], align="left", width=6, height=4)
x_pi = PushButton(app, command=say_my_name, text="π", grid=[7,3], align="left", width=6, height=4)
x_e = PushButton(app, command=say_my_name, text="e", grid=[7,4], align="left", width=6, height=4)
x_x_squared = PushButton(app, command=say_my_name, text="x²", grid=[8,4], align="left", width=6, height=4)
x_x_power = PushButton(app, command=say_my_name, text="x^n", grid=[9,4], align="left", width=6, height=4)
input_right = PushButton(app, command=say_my_name, text=">", grid=[9,3], align="left", width=6, height=4)
input_left = PushButton(app, command=say_my_name, text="<", grid=[8,3], align="left", width=6, height=4)
x_ln = PushButton(app, command=say_my_name, text="ln", grid=[10,2], align="left", width=6, height=4)
x_log = PushButton(app, command=say_my_name, text="log", grid=[10,3], align="left", width=6, height=4)







app.display()
