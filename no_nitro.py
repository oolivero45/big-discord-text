from tkinter import Tk
text = input("Enter text: ").lower()
output = ""
for i in text:
    if i == " ":
        output += "    "
    elif i == "!":
        output += ":exclamation: "
    elif i == "?":
        output += ":question: "
    elif i == "+":
        output += ":heavy_plus_sign: "
    elif i == "-":
        output += ":heavy_minus_sign: "
    elif i == "$":
        output += ":heavy_dollar_sign: "
    elif i in [".",",","(",")","[","]","'",'"',"£","%","^","&","*","_","=",":",";","@","#","~","\\","|","¬","`"]:
        output += i + " "
    else:
        output += ":regional_indicator_" + i + ": "

print(output)
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(output)
r.destroy()
print("\nText added to clipboard.")
