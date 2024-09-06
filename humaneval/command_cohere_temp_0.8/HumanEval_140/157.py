```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) == 0 or new_text[-1] != '-':
                new_text.append('_')
            else:
                new_text.append(c)
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The code uses a simple loop to iterate through the input text. When the current character is a space, it checks the previous character to determine whether to replace the space with an underscore or a - sign. All other characters are added to the new_text list as is. Finally, the function joins the list to produce the required output string.