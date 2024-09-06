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

The function iterates through the input `text` and uses a conditional check to determine whether or not a character is a space. If the character is a space, it checks the previous character; if it's not an `-`, it replaces the space with an `_`, otherwise, it replaces the space with itself. This ensures that all spaces are replaced correctly while preserving the two-space threshold.