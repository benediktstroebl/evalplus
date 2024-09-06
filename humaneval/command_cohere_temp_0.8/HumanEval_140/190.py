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

The function goes through each character in the input `text` and either appends an underscore or itself into a list `new_text` depending on whether the character is a space or not. If the character is a space, the code checks the previous element added if it was an underscore or not. If it was an underscore, the space is also converted to an underscore, otherwise, it is kept as it is. The final string is obtained by joining `new_text`.