```python
def fix_spaces(text):
    new_text = []
    for char in text:
        if char == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ' and new_text[-2] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(char)
    return ''.join(new_text)
``` 

The code iterates through every character of the input `text`, and whenever it encounters an space, it checks the previous two characters. If they are both spaces, it replaces the current space with `-`, otherwise it replaces it with an underscore. The resulting string is then returned as the output. 

This code solves the problem statement and is easy to use and understand.