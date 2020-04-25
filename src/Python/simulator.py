from tkinter import *
from PIL import Image
from PIL import ImageTk
from Python.menubar import MenuBar
from Python.breadboard import Breadboard
from Python.wire import Wire
from Python.wire import WireEdit
from Python.resistor import Resistor
from Python.led import LED
from Python.powersupply import PowerSupply
from Python.powersupply import PowerSupplyEdit
from Python.switch import Switch

class Simulator(Frame):
    def __init__(self, master):
        """ Simulator(master): creates a new Simulator object
        Simulator object has a display at the bottom as well as many holes and labels
        :param master: (Tk) """

        Frame.__init__(self, master, bg = "white")
        self.grid()
        self.length = 52
        self.height = 19

        self.display = Label(self, bg = "white", font = ("Arial", 48))
        self.display.grid(row = self.height + 1, column = 0, columnspan = self.length)

        self.wirestarts = {}
        self.wireends ={}
        self.wireimg = ImageTk.PhotoImage(Image.open("wire.jpg").resize((50, 50), Image.ANTIALIAS))
        self.wirepic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.wirepic.create_image(27, 27, image = self.wireimg)
        self.wirepic.image = self.wireimg
        self.wirepic.grid(row = self.height, column = 1, columnspan = 9)
        self.wirepic.bind("<Button>", self.wire_select)

        self.resistors = []
        self.resistorimg = ImageTk.PhotoImage(Image.open("resistor.jpg").resize((50, 50), Image.ANTIALIAS))
        self.resistorpic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.resistorpic.create_image(27, 27, image = self.resistorimg)
        self.resistorpic.image = self.resistorimg
        self.resistorpic.grid(row = self.height, column = 11, columnspan = 9)
        self.resistorpic.bind("<Button>", self.resistor_select)

        self.leds = []
        self.ledimg = ImageTk.PhotoImage(Image.open("led.jpg").resize((50, 50), Image.ANTIALIAS))
        self.ledpic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.ledpic.create_image(27, 27, image = self.ledimg)
        self.ledpic.image = self.ledimg
        self.ledpic.grid(row = self.height, column = 21, columnspan = 9)
        self.ledpic.bind("<Button>", self.led_select)

        self.supplies = {}
        self.voltages = {}
        self.powersupplyimg = ImageTk.PhotoImage(Image.open("powersupply.jpg").resize((50, 50), Image.ANTIALIAS))
        self.powersupplypic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.powersupplypic.create_image(27, 27, image = self.powersupplyimg)
        self.powersupplypic.image = self.powersupplyimg
        self.powersupplypic.grid(row = self.height, column = 31, columnspan = 9)
        self.powersupplypic.bind("<Button>", self.powersupply_select)

        self.switchs = []
        self.switchimg = ImageTk.PhotoImage(Image.open("switch.jpg").resize((50, 50), Image.ANTIALIAS))
        self.switchpic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.switchpic.create_image(27, 27, image = self.switchimg)
        self.switchpic.image = self.switchimg
        self.switchpic.grid(row = self.height, column = 41, columnspan = 9)
        self.switchpic.bind("<Button>", self.switch_select)

        self.elements = {}
        self.groups = {}
        self.breadboard = Breadboard(self, self.length, self.height)
        self.breadboard.reset()

    def reset_highlight(self):
        self.wirepic["highlightbackground"] = "white"
        self.resistorpic["highlightbackground"] = "white"
        self.ledpic["highlightbackground"] = "white"
        self.powersupplypic["highlightbackground"] = "white"
        self.switchpic["highlightbackground"] = "white"

    def reset(self):
        self.elements = self.breadboard.elements
        self.groups = self.breadboard.groups
        self.grid_breadboard()
        self.display["text"] = ""
        self.reset_highlight()

    def grid_breadboard(self):
        for row in range(0, self.height):
            for column in range(0, self.length):
                coord = (row, column)
                self.elements[coord].grid(row = row, column = column)

    def wire_select(self, event):
        self.reset_highlight()
        self.wirepic["highlightbackground"] = "gold"

        root = Tk()
        root.title("New Wire")
        wire = Wire(root, self)
        wire.mainloop()

    def wire_edit(self, coord):
        root = Tk()
        root.title("Edit Wire")
        wire = WireEdit(root, self.elements[coord], self)
        wire.mainloop()

    def resistor_select(self, event):
        self.reset_highlight()
        self.resistorpic["highlightbackground"] = "gold"

    def led_select(self, event):
        self.reset_highlight()
        self.ledpic["highlightbackground"] = "gold"

    def powersupply_select(self, event):
        self.reset_highlight()
        self.powersupplypic["highlightbackground"] = "gold"

        root = Tk()
        root.title("New Power Supply")
        powersupply = PowerSupply(root, self)
        powersupply.mainloop()

    def powersupply_edit(self, coord):
        root = Tk()
        root.title("Edit Power Supply")
        powersupply = PowerSupplyEdit(root, self.elements[coord], self)
        powersupply.mainloop()

    def switch_select(self, event):
        self.reset_highlight()
        self.switchpic["highlightbackground"] = "gold"

# Run Simulator
root = Tk()
root.title("Breadboard Simulator")
sim = Simulator(root)
menu = Menu(root)
menubar = MenuBar(root, menu, sim)
root.config(menu = menu)
sim.mainloop()