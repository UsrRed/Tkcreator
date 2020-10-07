import tkinter as tk


class TkModule:

    def __init__(self, cv, csv_file):
        self.cv = cv
        self.csv_file = csv_file
        self.list_save = []
        self.widget = None
        self.entry = None
        self.arg_selected = None

    def select(self, widget):
        self.widget = widget
        self.list_save.append(self.widget)

    def get(self):
        return self.widget

    def delete(self):
        if self.widget:
            self.widget.destroy()
            self.widget = None
            self.list_save.pop(len(self.list_save) - 1)
            # select the previous widget
            if self.list_save:
                self.widget = self.list_save[len(self.list_save) - 1]

    def get_config(self):
        my_list = []
        for item in self.widget.keys():
            my_list.append([item, self.widget.cget(item)])
        return my_list

    def add_arg(self, arg, value):
        self.widget[arg] = value

    def get_change(self):
        list_config = []
        classe = self.widget.winfo_class()
        if classe == "Labelframe":
            classe = "LabelFrame"
        compar = getattr(tk, classe)()
        for item in self.widget.keys():
            if str(self.widget.cget(item)) != "" and self.widget.cget(item) != compar.cget(item):
                list_config.append([item, self.widget.cget(item)])
        my_string = "\t\t\t\t\t\t\t\t\t\t\t\nArguments :"
        txt1 = ""
        for x in list_config:
            if list_config.index(x) % 2 == 0:
                txt1 = str(x[0]) + " = " + str(x[1])
                my_string += "\n" + txt1
            else:
                add = int((50 - len(txt1) * 1.6)) * " "
                my_string += add + "\t" + str(x[0]) + " = " + str(x[1]) + "\t"
        my_string += "\n"
        if not list_config:
            my_string = ""
        return my_string
