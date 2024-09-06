```python
def fix_spaces(text):
    new_text = []
    for char in text:
        if char == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(char)
    return ''.join(new_text)
``` 

The code uses a for loop to iterate through each character in the `text` string. When it encounters a space, it checks the previous character; if it was also a space, it means there are more than 2 consecutive spaces, so it replaces the space with `-`. Otherwise, it replaces the space with an `_`. All other characters remain the same. The resulting string is then returned.