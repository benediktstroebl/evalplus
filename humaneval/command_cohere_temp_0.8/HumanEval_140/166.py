```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ' and new_text[-2] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The code uses a for loop to iterate through each character in the input text. When it encounters a space, it checks the previous two characters. If they are both spaces, it replaces the space with `-`, otherwise, it replaces the space with an underscore. The resulting string is then returned.