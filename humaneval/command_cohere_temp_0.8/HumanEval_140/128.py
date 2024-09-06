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

The code uses a for loop to iterate over each character in the `text` string. When it encounters a space, it checks the previous character; if it was also a space, it means there are more than 2 consecutive spaces, so it replaces the spaces with a '-'. Otherwise, it replaces the space with an underscore. All other characters remain unchanged as they are appended to the `new_text` list. Finally, the function returns a string concatenation of the `new_text` list. 

This solution allows for efficient processing of the text and achieves the desired result.