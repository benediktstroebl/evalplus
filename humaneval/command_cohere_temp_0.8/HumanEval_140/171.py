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

The code uses a loop to iterate through each character of the input `text`. When it encounters a space, it checks the character that precedes this space. If it's not an '-', then it replaces the space with an `_`. Otherwise, it keeps the space. This way, the code achieves the desired output as stated in the problem statement.