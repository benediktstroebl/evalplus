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

The code solves the problem using a relatively simple approach, only one pass is needed through the text to be fixed. When iterating through every character of the text, if the character is a space, the code checks the previous character, if it was also a space, meaning consecutive spaces, they are replaced by a single -, otherwise, all spaces are replaced with an underscore. Then the resulting string is joined and returned.