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

The code uses a loop to iterate through each character in the input `text`. When it encounters a space, it checks the previous character; if it's not an `-` (i.e., if the previous character is not a hyphen or the last character in the text), it replaces the space with an `_` (underscore). Otherwise, it keeps the space. This ensures that all consecutive spaces are replaced with `_` except for spaces preceded by a hyphen.