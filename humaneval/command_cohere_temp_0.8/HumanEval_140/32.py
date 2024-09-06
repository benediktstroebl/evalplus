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

The code uses a for loop to iterate over each character in the `text` string. When it encounters a space, it checks the previous character; if it was also a space, it appends a `-` to the `new_text` list, otherwise, it appends an underscore. For all other characters, it appends the character as is to `new_text`. Finally, the function returns the joined string of the `new_text` list.

This approach ensures that all spaces are correctly replaced, and consecutive spaces are replaced by hyphens.