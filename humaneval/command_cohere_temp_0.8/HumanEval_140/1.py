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

The function iterates through the input text, and for each character, it checks if it is a space. If it is, it checks the previous character; if it's not an `-`, it replaces the space with an `_`, otherwise, it keeps the space. 

This solution is concise and easy to understand while still correctly solving the problem and meeting the specifications of the given challenge.