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

The code uses a list to build the new string, ensuring that all spaces are correctly replaced. The case of multiple consecutive spaces is handled by checking the previous two elements in the list, if they are both spaces, then it replaces the current space with a `-`. Otherwise, it replaces the space with an `_`. The rest of the characters are appended to the list as is.