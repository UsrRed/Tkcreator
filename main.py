from tkinter.filedialog import asksaveasfilename

from tkinter import colorchooser
from time import sleep
import simplejson as json
import threading
from classe import *

# initialise
root = tk.Tk()
root.title("Tkmodule")
root.configure(bg="Grey")
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry(str(int(x / 1.3)) + "x" + str(int(y / 1.7)))

text_show = ""

# Canvas contain all widgets, workplace
cv = tk.Canvas(root, bg="Grey")
cv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# percentage of root
x_percent = int(x / 170)
y_percent = int(y / 170)
mod = TkModule(cv, "save")

# Config menu
background = "#D0D0D0"
conf = tk.LabelFrame(root, text="No widget selected", bg=background)
conf.pack(side=tk.RIGHT, fill=tk.Y)

# Menu bar
menuBar = tk.Menu(root)
root.config(menu=menuBar)
widget_menu = tk.Menu(menuBar, tearoff=0)
save_type = tk.Menu(menuBar, tearoff=0)
open_type = tk.Menu(menuBar, tearoff=0)
indicator = tk.StringVar()
indicator.set("Widget selected : None")


# configure frame
def configure_start():
    # Placement
    topframe = tk.LabelFrame(conf, bg=background, text="Select argument")
    topframe_1 = tk.Frame(topframe, bg=background)
    topframe_2 = tk.Frame(topframe, bg=background)
    topframe_3 = tk.Frame(topframe, bg=background)
    topframe_4 = tk.Frame(topframe, bg=background)
    topframe_5 = tk.Frame(topframe, bg=background)
    topframe_box = [topframe_1, topframe_2, topframe_3, topframe_4, topframe_5]
    topframe.pack(fill=tk.BOTH, padx=1, pady=1)
    topframe_1.pack(fill=tk.BOTH)
    topframe_2.pack(fill=tk.BOTH)
    topframe_3.pack(fill=tk.BOTH)
    topframe_4.pack(fill=tk.BOTH)
    topframe_5.pack(fill=tk.BOTH)
    middleframe = tk.LabelFrame(conf, bg=background, text="Module", width=5)
    middleframe.pack(fill=tk.BOTH, padx=1, pady=1)
    bottomframe = tk.LabelFrame(conf, bg=background, text="Change value")
    bottomframe.pack(fill=tk.BOTH, padx=1, pady=1)

    # change value of an argument
    txt = tk.StringVar()
    mod.entry = tk.Entry(bottomframe, textvariable=txt)
    label_change = tk.Label(conf, text="\t\t\t\t\t\t\t\t\t\t\t", justify='left', bg=background)

    button_list = []
    var_button = tk.StringVar()

    def change(*evt):
        if mod.get():
            try:
                mod.add_arg(var_button.get(), mod.entry.get())
            except:
                show("Invalid entry:\n" + str(var_button.get()) + "=" + str(mod.entry.get()))
            label_change.configure(text=mod.get_change())

    mod.entry.bind("<Return>", change)
    btn_modif = tk.Button(bottomframe, text="Change", command=change, cursor="sb_right_arrow")

    def act_module():
        for w_module in middleframe.winfo_children():
            w_module.destroy()
        arg = var_button.get()

        def change_value(value):
            txt.set(value)
            if value:
                change()
            for w_module_ in middleframe.winfo_children():
                w_module_.destroy()

        # colorchooser
        list_colorchooser = ["bg", "background", "activebackground", "activeforeground", "fg", "foreground",
                             "disabledbackground", "disabledforeground", "highlightbackground", "highlightcolor",
                             "insertbackground", "readonlybackground", "selectbackground", "selectforeground",
                             "selectcolor"]
        if arg in list_colorchooser:
            module = colorchooser.askcolor()
            if module[1]:
                change_value(module[1])

        # all module associated to some arguments to make them easier to use
        if arg == "justify":
            btn_left = tk.Button(middleframe, text="LEFT", command=lambda: change_value("left"))
            btn_center = tk.Button(middleframe, text="CENTER", command=lambda: change_value("center"))
            btn_right = tk.Button(middleframe, text="RIGHT", command=lambda: change_value("right"))
            btn_left.pack(side=tk.LEFT, padx=2, pady=2)
            btn_center.pack(side=tk.LEFT, padx=2, pady=2)
            btn_right.pack(side=tk.LEFT, padx=2, pady=2)

        if arg == "anchor":
            temp_top = tk.Frame(middleframe, bg=background)
            temp_top.pack()
            temp_mid = tk.Frame(middleframe, bg=background)
            temp_mid.pack()
            temp_bot = tk.Frame(middleframe, bg=background)
            temp_bot.pack()
            btn_nw = tk.Button(temp_top, text="NW", command=lambda: change_value("nw"))
            btn_n = tk.Button(temp_top, text="N", command=lambda: change_value("n"))
            btn_ne = tk.Button(temp_top, text="NE", command=lambda: change_value("ne"))
            btn_w = tk.Button(temp_mid, text="W", command=lambda: change_value("w"))
            btn_center = tk.Button(temp_mid, text="CENTER", command=lambda: change_value("center"))
            btn_e = tk.Button(temp_mid, text="E", command=lambda: change_value("e"))
            btn_sw = tk.Button(temp_bot, text="SW", command=lambda: change_value("sw"))
            btn_s = tk.Button(temp_bot, text="S", command=lambda: change_value("s"))
            btn_se = tk.Button(temp_bot, text="SE", command=lambda: change_value("se"))
            btn_nw.pack(side=tk.LEFT, padx=2, pady=2)
            btn_n.pack(side=tk.LEFT, padx=2, pady=2)
            btn_ne.pack(side=tk.LEFT, padx=2, pady=2)
            btn_w.pack(side=tk.LEFT, padx=2, pady=2)
            btn_center.pack(side=tk.LEFT, padx=2, pady=2)
            btn_e.pack(side=tk.LEFT, padx=2, pady=2)
            btn_sw.pack(side=tk.LEFT, padx=2, pady=2)
            btn_s.pack(side=tk.LEFT, padx=2, pady=2)
            btn_se.pack(side=tk.LEFT, padx=2, pady=2)

        if arg == "cursor":
            var_cursor = tk.StringVar()

            def select_cursor():
                change_value(var_cursor.get())

            list_cursor = ["arrow", "man", "based_arrow_down", "middlebutton", "based_arrow_up", "mouse", "boat",
                           "pencil", "bogosity", "pirate", "bottom_left_corner", "plus", "bottom_right_corner",
                           "question_arrow", "bottom_side", "right_ptr", "bottom_tee", "right_side",
                           "box_spiral", "right_tee", "center_ptr", "rightbutton", "circle", "rtl_logo", "clock",
                           "sailboat", "coffee_mug", "sb_down_arrow", "cross", "sb_h_double_arrow", "cross_reverse",
                           "sb_left_arrow", "crosshair", "sb_right_arrow", "diamond_cross", "sb_up_arrow", "dot",
                           "sb_v_double_arrow", "dotbox", "shuttle", "double_arrow", "sizing", "draft_large", "spider",
                           "draft_small", "spraycan", "draped_box", "star", "exchange", "target", "fleur", "tcross",
                           "gobbler", "top_left_arrow", "gumby", "top_left_corner", "hand1", "top_right_corner",
                           "hand2", "top_side", "heart", "top_tee", "icon", "trek", "iron_cross", "ul_angle",
                           "left_ptr", "umbrella", "left_side", "ur_angle", "left_tee", "watch", "leftbutton", "xterm",
                           "ll_angle", "X_cursor", "lr_angle"]
            box = []
            for box_count in range(9):
                frame = tk.Frame(middleframe, bg=background)
                frame.pack()
                box.append(frame)
            for cursor in list_cursor:
                btn_cursor = tk.Radiobutton(box[int(list_cursor.index(cursor)/len(list_cursor)*len(box))],
                                            variable=var_cursor, cursor=cursor, text=str(cursor), value=cursor,
                                            indicatoron=0, command=select_cursor)
                btn_cursor.pack(padx=1, pady=1, side=tk.LEFT)

        if arg == "state" or arg == "default":
            btn_dis = tk.Button(middleframe, text="Disabled", command=lambda: change_value("disabled"))
            btn_dis.pack(side=tk.LEFT, padx=2, pady=2)
            btn_norm = tk.Button(middleframe, text="Normal", command=lambda: change_value("normal"))
            btn_norm.pack(side=tk.LEFT, padx=2, pady=2)
            if arg == "state":
                btn_act = tk.Button(middleframe, text="Active", command=lambda: change_value("active"))
                btn_act.pack(side=tk.LEFT, padx=2, pady=2)

        if arg == "relief" or arg == "overrelief" or arg == "offrelief":
            btn_flat = tk.Button(middleframe, text="FLAT", command=lambda: change_value("flat"), relief="flat")
            btn_flat.pack(side=tk.LEFT, padx=2, pady=2)
            btn_raised = tk.Button(middleframe, text="RAISED", command=lambda: change_value("raised"), relief="raised")
            btn_raised.pack(side=tk.LEFT, padx=2, pady=2)
            btn_sunken = tk.Button(middleframe, text="SUNKEN", command=lambda: change_value("sunken"), relief="sunken")
            btn_sunken.pack(side=tk.LEFT, padx=2, pady=2)
            btn_groove = tk.Button(middleframe, text="GROOVE", command=lambda: change_value("groove"), relief="groove")
            btn_groove.pack(side=tk.LEFT, padx=2, pady=2)
            btn_ridge = tk.Button(middleframe, text="RIDGE", command=lambda: change_value("ridge"), relief="ridge")
            btn_ridge.pack(side=tk.LEFT, padx=2, pady=2)

        if arg == "bitmap":
            btn_error = tk.Button(middleframe, text="error", command=lambda: change_value("error"), bitmap="error")
            btn_error.pack(side=tk.LEFT, padx=2, pady=2)
            btn_gray75 = tk.Button(middleframe, text="gray75", command=lambda: change_value("gray75"), bitmap="gray75")
            btn_gray75.pack(side=tk.LEFT, padx=2, pady=2)
            btn_gray50 = tk.Button(middleframe, text="gray50", command=lambda: change_value("gray50"), bitmap="gray50")
            btn_gray50.pack(side=tk.LEFT, padx=2, pady=2)
            btn_gray25 = tk.Button(middleframe, text="gray25", command=lambda: change_value("gray25"), bitmap="gray25")
            btn_gray25.pack(side=tk.LEFT, padx=2, pady=2)
            btn_gray12 = tk.Button(middleframe, text="gray12", command=lambda: change_value("gray12"), bitmap="gray12")
            btn_gray12.pack(side=tk.LEFT, padx=2, pady=2)
            btn_hourglass = tk.Button(middleframe, text="hourglass", command=lambda: change_value("hourglass"),
                                      bitmap="hourglass")
            btn_hourglass.pack(side=tk.LEFT, padx=2, pady=2)
            btn_info = tk.Button(middleframe, text="info", command=lambda: change_value("info"), bitmap="info")
            btn_info.pack(side=tk.LEFT, padx=2, pady=2)
            btn_questhead = tk.Button(middleframe, text="questhead", command=lambda: change_value("questhead"),
                                      bitmap="questhead")
            btn_questhead.pack(side=tk.LEFT, padx=2, pady=2)
            btn_question = tk.Button(middleframe, text="question", command=lambda: change_value("question"),
                                     bitmap="question")
            btn_question.pack(side=tk.LEFT, padx=2, pady=2)
            btn_warning = tk.Button(middleframe, text="warning", command=lambda: change_value("warning"),
                                    bitmap="warning")
            btn_warning.pack(side=tk.LEFT, padx=2, pady=2)

        if arg == "compound":
            bitmap = "question"
            btn_bottom = tk.Button(middleframe, text="bottom", command=lambda: change_value("bottom"),
                                   compound="bottom", bitmap=bitmap)
            btn_bottom.pack(side=tk.LEFT, padx=4, pady=2)
            btn_top = tk.Button(middleframe, text="top", command=lambda: change_value("top"), compound="top",
                                bitmap=bitmap)
            btn_top.pack(side=tk.LEFT, padx=4, pady=2)
            btn_left = tk.Button(middleframe, text="left", command=lambda: change_value("left"), compound="left",
                                 bitmap=bitmap)
            btn_left.pack(side=tk.LEFT, padx=4, pady=2)
            btn_right = tk.Button(middleframe, text="right", command=lambda: change_value("right"), compound="right",
                                  bitmap=bitmap)
            btn_right.pack(side=tk.LEFT, padx=4, pady=2)
            btn_center = tk.Button(middleframe, text="center", command=lambda: change_value("center"),
                                   compound="center", bitmap=bitmap)
            btn_center.pack(side=tk.LEFT, padx=4, pady=2)

    def select():
        act_module()

    def reset():
        txt.set("")
        label_change.configure(text="\t\t\t\t\t\t\t\t\t\t\t")

    # placing
    mod.entry.pack(side=tk.LEFT, fill=tk.BOTH, padx=1, pady=1)
    btn_modif.pack(side=tk.LEFT, fill=tk.BOTH, padx=1, pady=1)
    label_change.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=5, pady=5)

    register = ""
    chg = True
    while True:
        if mod.get():
            if mod.get() != register:
                reset()
                for button in button_list:
                    button.destroy()
                button_list = []
                chg = True
            else:
                chg = False
        if mod.get() and chg:
            conf.configure(text="Configuration - " + str(mod.get().winfo_name()))

            # create variables
            list_config = mod.get_config()
            list_arg = []
            for i in range(len(list_config)):
                list_arg.append((list_config[i][0]))

            label_change.configure(text=mod.get_change())

            # add arguments buttons
            n = int(len(list_arg)/4.5)
            for item in list_arg:
                rank = int(list_arg.index(item)/n)
                if rank > 4:
                    rank = 4
                b = tk.Radiobutton(topframe_box[rank], variable=var_button, text=str(item), value=item, indicatoron=0,
                                   command=select)
                b.pack(padx=1, pady=1, side=tk.LEFT, fill=tk.BOTH)
                button_list.append(b)

        elif chg:
            reset()
            for button in button_list:
                button.destroy()
            button_list = []
            conf.configure(text="No widget selected")

        register = mod.get()
        try:
            conf.update()
            conf.update_idletasks()
        except IOError:
            pass
        sleep(1)


th_configure = threading.Thread(target=configure_start)
th_configure.start()


#  to show a text like "export is done" no console and screen
def show_():
    print(text_show)
    msg = tk.Label(root, text=text_show)
    msg.pack(side=tk.TOP, fill=tk.X, padx=1, pady=1, expand=True)
    sleep(len(text_show) // 5 + 2.5)
    msg.destroy()


# start show function
def show(text):
    global text_show
    text_show = text
    th_show = threading.Thread(target=show_)
    th_show.start()


# create a widget
def w_call(widget_class):
    mod.select(getattr(tk, widget_class)(cv))
    widget_menu.entryconfig(0, label="Widget selected : " + widget_class)


# function to save the widgets and her parameters
def save(file):
    f = open(file, "w")
    data = {}
    n = 0
    for widget in mod.list_save:
        widget_class = widget.winfo_class()
        if widget_class == "Labelframe":
            widget_class = "LabelFrame"

        parent_id = widget.winfo_parent()

        arguments = {}
        widget_compar = getattr(tk, widget_class)()
        for item in widget.keys():
            if widget_compar.cget(item) != widget.cget(item):
                if str(widget.cget(item)) != "":
                    arguments.update({str(item): widget.cget(item)})

        parent = cv.nametowidget(parent_id)
        # size of the parent to place with percent (adapt to screen)
        p_size = parent.winfo_geometry().split("+")[0].split("x")
        x_ = int(p_size[0])
        y_ = int(p_size[1])
        # get the coord of widget
        coord = widget.winfo_geometry().split("+")
        # transform
        w_coord = str(int(coord[1]) / x_) + ":" + str(int(coord[2]) / y_)

        data.update({"widget" + str(n): {"widget_class": widget_class, "parent_id": parent_id,
                                         "arguments": arguments, "w_coord": w_coord}})
        n += 1
    f.write(json.dumps(data))
    f.close()


# Quick save
def save_recent(*event):
    save("save.json")
    show("Quick save is done")


# Save and choose the folder
def save_tkmodule():
    file = asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")],
                             title="Save file")
    save(file)
    show("Save is done")


# Open the saving file with all widget and create them
def open_(file):
    f = open(file, "r+")
    data = json.loads(f.read())
    for widget_brut in data:
        # creating widget
        widget = getattr(tk, data[widget_brut]["widget_class"])(cv.nametowidget(data[widget_brut]["parent_id"]))
        mod.list_save.append(widget)

        # adding configs
        for item in data[widget_brut]["arguments"]:
            widget[item] = data[widget_brut]["arguments"][item]

        x_, y_ = data[widget_brut]["w_coord"].split(":")
        widget.place(relx=x_, rely=y_)
    f.close()


# quick open
def open_recent():
    open_("save.json")


# select opening file
def open_tkmodule():
    file = asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")],
                             title="Open file")
    open_(file)


# generate the script with all widgets
def export():
    file = asksaveasfilename(defaultextension=".py", filetypes=[("PY", "*.py")],
                             title="Export to python file")
    text = ""
    list_widget = []
    list_string_force = ["text", "cursor", "justify", "overrelief", "relief", "state", "variable", "compound", "bitmap",
                         "offrelief", "anchor", "default", "bg", "background", "activebackground", "activeforeground",
                         "fg", "foreground", "disabledbackground", "disabledforeground", "highlightbackground",
                         "highlightcolor", "insertbackground", "readonlybackground", "selectbackground",
                         "selectforeground", "scrollregion", "selectcolor", "show", "activestyle", "direction",
                         "orient", "sashrelief", "label", "troughcolor", "wrap"]
    list_widget_func = ["Button"]
    for widget in mod.list_save:
        if widget.winfo_ismapped:
            arguments = []
            # get all arguments
            name = widget.winfo_class()
            if name == "Labelframe":
                name = "LabelFrame"
            widget_compar = getattr(tk, name)()
            for item in widget.keys():
                if widget_compar.cget(item) != widget.cget(item):
                    if str(widget.cget(item)) != "":
                        arg = widget.cget(item)
                        if item in list_string_force:
                            arg = '"' + str(arg) + '"'
                        arguments.append(str(item) + "=" + str(arg))

            widget_compar.destroy()

            p_size = cv.winfo_geometry().split("+")[0].split("x")
            x_size, y_size = int(p_size[0]), int(p_size[1])
            coord = widget.winfo_geometry().split("+")
            x_, y_ = str(int(coord[1]) / x_size), str(int(coord[2]) / y_size)

            # append the name, class, arguments, coords
            list_widget.append((widget.winfo_name().split("!")[1], widget.winfo_class(), arguments,
                                (x_, y_)))
    list_class_use = []
    for wi in list_widget:
        if wi[1] not in list_class_use:
            list_class_use.append(wi[1])
    if list_class_use:
        # imports
        text += "from tkinter import Tk, "
        for imp in list_class_use:
            if imp != list_class_use[len(list_class_use) - 1]:
                text += imp + ", "
            else:
                text += imp

        text += "\n\n\n"

        # initialisation root
        list_arg_root = []
        test = tk.Canvas()
        list_forbid_arg = ["insertbackground", "scrollregion", "selectbackground", "selectforeground", "state"]
        for item in cv.keys():
            if item not in list_forbid_arg:
                if item in list_string_force:
                    arg = "'" + cv.cget(item) + "'"
                    list_arg_root.append(item + "=" + arg)
                else:
                    if cv.cget(item) != test.cget(item):
                        arg = cv.cget(item)
                        list_arg_root.append(item + "=" + arg)
        test.destroy()
        arg_root = ", ".join(list_arg_root)
        text += "root = Tk()\n" \
                "root.title('root')\n" \
                "root.geometry('" + cv.winfo_geometry().split("+")[0] + "')\n" \
                                                                        "root.configure(" + arg_root + ")\n\n\n"

        # creation of function require
        for widget in list_widget:
            if widget[1] in list_widget_func:
                text += "def " + widget[0] + "_function():\n" \
                                             "\tpass\n\n\n"

        # create widgets
        for widget in list_widget:
            args = ", ".join(widget[2])
            if widget[1] in list_widget_func:
                add = "command=lambda: " + widget[0] + "_function()"
                if widget[2]:
                    add += ", "
            else:
                add = ""
            if add != "" or args != "":
                synt = ", "
            else:
                synt = ""
            text += widget[0] + " = " + widget[1] + "(root" + synt + add + args + ")\n"

        text += "\n\n"
        for widget in list_widget:
            text += widget[0] + ".place(relx=" + widget[3][0] + ", rely=" + widget[3][1] + ")\n"
        text += "\n\nroot.mainloop()\n"
        f = open(file, "w")
        f.write(text)
        f.close()
        show("Export is done")


# to select the canvas, that permit you to configure the root like background = "blue"
def config_root():
    mod.widget = cv


# Menu bar
menuBar.add_cascade(label='Widgets', menu=widget_menu)
menuBar.add_separator()
menuBar.add_separator()
menuBar.add_command(label="Configure root", command=config_root)
menuBar.add_separator()
menuBar.add_separator()
# Save cascade on menu bar
menuBar.add_cascade(label='Save', menu=save_type)
save_type.add_command(label="Quick save", command=save_recent)
save_type.add_command(label="Save as...", command=save_tkmodule)
# Open cascade on menu bar
menuBar.add_cascade(label="Open", menu=open_type)
open_type.add_command(label="Quick open", command=open_recent)
open_type.add_command(label="Open ...", command=open_tkmodule)

menuBar.add_command(label="Export", command=export)

# widgets cascade on menu bar
widget_menu.add_command(label="Select a widget")
widget_menu.add_command(label='Button', command=lambda: w_call("Button"))
widget_menu.add_command(label='Label', command=lambda: w_call("Label"))
widget_menu.add_command(label='Entry', command=lambda: w_call("Entry"))
widget_menu.add_command(label='Checkbutton', command=lambda: w_call("Checkbutton"))
widget_menu.add_command(label='Radiobutton', command=lambda: w_call("Radiobutton"))
widget_menu.add_command(label='Listbox', command=lambda: w_call("Listbox"))
widget_menu.add_command(label='Canvas', command=lambda: w_call("Canvas"))
widget_menu.add_command(label='Scale', command=lambda: w_call("Scale"))
widget_menu.add_command(label='Frame', command=lambda: w_call("Frame"))
widget_menu.add_command(label='Spinbox', command=lambda: w_call("Spinbox"))
widget_menu.add_command(label='LabelFrame', command=lambda: w_call("LabelFrame"))


# delete widget selected or the previous
def delete(event):
    if root.focus_get() != mod.entry:
        mod.delete()
        widget_menu.entryconfig(0, label="Select a widget")


# mouse events
def left_click(event):
    widget_on_mouse = root.winfo_containing(event.x_root, event.y_root)
    # detect if you click on a widget or just on the workplace
    if widget_on_mouse == cv:
        # place widget
        if mod.get() and mod.get() != cv:
            x_root, y_root = root.winfo_geometry().split("+")[1:]
            x_cv, y_cv = cv.winfo_geometry().split("+")[0].split("x")
            x_real = (event.x_root - int(x_root) - 10) / int(x_cv)
            y_real = (event.y_root - int(y_root) - 50) / int(y_cv)
            mod.get().place(relx=x_real, rely=y_real)
    elif widget_on_mouse in mod.list_save:
        # select the widget
        mod.select(widget_on_mouse)
        mod.list_save.pop(mod.list_save.index(widget_on_mouse))


# right click to show widgets selector
def pop_widget(event):
    widget_menu.post(event.x_root, event.y_root)


root.bind("<Button-1>", left_click)
root.bind("<Button-2>", pop_widget)
root.bind("<BackSpace>", delete)
root.bind("<Control-z>", delete)
root.bind("<Control-Z>", delete)
root.bind("<Control-s>", save_recent)
root.bind("<Control-S>", save_recent)

root.mainloop()
