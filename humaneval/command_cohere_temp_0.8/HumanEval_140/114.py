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

The code uses a simple loop to iterate through the input `text`, and consciously inspects the previous character (`new_text`[-1]]), and intelligently decides to replace spaces with `_` or `-` accordingly. This solution is efficient and easy to understand.