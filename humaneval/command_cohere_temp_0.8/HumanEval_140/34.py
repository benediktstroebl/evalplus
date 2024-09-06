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

The code uses a loop to iterate through each character in the `text` string. When it encounters a space, it checks the previous character; if it's not an '-', it replaces the space with an underscore. Otherwise, it keeps the space. This strategy solves the problem without using any built-in methods that could handle strings, making it compatible with Python 3.5.

This approach allows the code to be self-contained, relying only on basic Python data types and operations. It is also efficient, with a time complexity of O(n), where n is the length of the input text.