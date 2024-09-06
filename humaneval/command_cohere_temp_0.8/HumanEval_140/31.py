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

The function `fix_spaces` iterates through each character in the input `text`. When it encounters a space, it checks the previous character; if it's not an `-` then it replaces the space with an `_`, otherwise, it keeps the space. This strategy solves the problem without any additional utilities needed.