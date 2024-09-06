```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The function `fix_spaces()` goes through the characters of the input text one by one. When it encounters a space, it checks the previous character; if it's also a space, it means there are more than two consecutive spaces, so it replaces the current space with a `-`. Otherwise, it replaces the space with an `_`. In either case, the character is appended to the `new_text` list. The final string is joined from the list using `''.join(new_text)` and returned.