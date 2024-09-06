```python
def fix_spaces(text):
    new_text = []
    for char in text:
        if char == ' ':
            if len(new_text) == 0 or new_text[-1] != '-':
                new_text.append('_')
            else:
                new_text.append(char)
        else:
            new_text.append(char)
    return ''.join(new_text)
```

The function `fix_spaces` processes the input text character by character. When it encounters a space, it checks the previous character; if it's not an `-`, an `_` will be appended to the `new_text` list. Otherwise, the current space will be appended. The resulting string is then joined from the `new_text` list.