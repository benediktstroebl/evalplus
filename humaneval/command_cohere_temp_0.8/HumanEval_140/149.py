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

The code uses a for loop to iterate through each character in the `text` string. When it encounters a space, it checks the previous character; if it was also a space, it means there are more than two consecutive spaces, so it replaces the spaces with a `-`. Otherwise, it replaces the space with an `_`. All other characters are appended to the `new_text` list unchanged. Finally, the function returns the joined string of the `new_text` list. 

This solution allows for efficient, single-pass processing of the input text and produces the desired output as stated in the problem.