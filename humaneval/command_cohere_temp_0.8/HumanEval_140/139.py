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

The function examines each character of the input `text`. If the character is a space, it checks the previous character in the `new_text` list. If the previous character is not `-`, it replaces the space with an underscore. Otherwise, it replaces the space with itself. For all other characters, it leaves them unchanged and appends them to `new_text`. Finally, the function joins the list of new text to form a single string and returns the result. 

This code solves the problem using only a list and a single loop, efficiently managing the replacement of spaces with underscores and dashes.