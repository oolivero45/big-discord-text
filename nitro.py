from tkinter import Tk
output = ""
prefix = "cyan_"
colours = ["red","orange","yellow","green","teal","blue","purple","pink","cyan", "rainbow"]
rainbowcolours = ["red","orange","yellow","green","teal","blue","purple","pink"]
rainbow = 0
rainbowmax = len(rainbowcolours)
print("Possible colours: ")
for i in range(0, len(colours)):
    print(" - " + colours[i])
colour = input("\nEnter a colour. If an invalid colour is given, or if it is left blank, cyan will be used: ").lower().replace("\n","")
if colour in colours:
    prefix = colour + "_"

text = input("Enter text: ").lower().replace("\n","")

for i in text:
    if colour == "rainbow":
        prefix = rainbowcolours[rainbow] + "_"
        rainbow += 1
        if rainbow == rainbowmax:
            rainbow = 0
    if i == " ":
        output += ":" + prefix + "space:"
    elif i == "!":
        output += ":" + prefix + "exclamation:"
    elif i == "?":
        output += ":" + prefix + "question:"
    elif i == ".":
        output += ":" + prefix + "fullstop:"
    elif i == ",":
        output += ":" + prefix + "comma:"
    elif i == "'":
        output += ":" + prefix + "apostrophe:"
    elif i in list("abcdefghijklmnopqrstuvwxyz1234567890"):
        output += ":" + prefix + i + ":"
    else:
        output += i + " "

print(output)
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(output)
r.destroy()
print("\nText added to clipboard.")
