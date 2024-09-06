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

The function iterates through the input `text` and uses a conditional check to determine whether or not to replace spaces with underscores or - for consecutive spaces. The result is then returned as a concatenated string. 

This approach allows for the replacement of consecutive spaces with the correct character, while also preserving single spaces as underscores.