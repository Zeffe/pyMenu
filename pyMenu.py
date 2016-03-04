import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

out = ""

content = []
command = {}

commands = 0

while True:
    cmdAmnt = raw_input(" [>] How many commands would you like to have?: ")
    try:
        if int(cmdAmnt) > 0:
            commands = int(cmdAmnt)
            break
        else:
            print "Amount must be numeric and greater than 0."
    except:
        print "Amount must be numeric and greater than 0."

clear()

content.append(raw_input(" [>] Credits: "))
print ""

for i in range(commands):
    content.append(raw_input(" [>] Command #" + str(i + 1) + ": "))
    command[content[i + 1]] = (raw_input(" [>] Command #" + str(i + 1) + " description: "))
    print ""

out = 'print "\\n Main Menu\\n\\n\\t' + content[0] + '\\n\\n Available Commands:\\n'

for i in content:
    if i is not content[0]:
        out += '\\n\\t' + i + '\\t\\t' + command[i]
out += '\\n"'

_file = open("menu.txt", "w")
_file.write(out)
_file.close()

clear()
print out
print ""
print "Exported to menu.txt in local directory."
raw_input()
