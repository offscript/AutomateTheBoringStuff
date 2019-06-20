#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste() #paste whatever is in the clipboard
separator = '\n' 

text_by_line = text.split('\n')
print(len(text_by_line))
for x in range(len(text_by_line)):
    text_by_line[x] = '*  ' + text_by_line[x]

return_text = separator.join(text_by_line)

pyperclip.copy(return_text)