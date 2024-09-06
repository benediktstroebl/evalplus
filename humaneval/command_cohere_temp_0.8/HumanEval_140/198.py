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

The code uses a for loop to iterate over each character in the `text` string. When it encounters a space, it checks the previous character; if it was also a space, it means there are more than two consecutive spaces, so it replaces the spaces with a `-`. Otherwise, it replaces the space with an `_`. All other characters remain the same. The resulting string is then joined back together with no spaces between the characters.