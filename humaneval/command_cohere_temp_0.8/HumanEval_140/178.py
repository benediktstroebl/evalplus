```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ' and new_text[-2] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The function goes through each character in the input `text` and either appends an underscore or a hyphen to the `new_text` list if the character is a space, depending on whether the previous two characters in `new_text` are also spaces. All non-space characters are appended unchanged to the resulting string. The resulting string joined from the `new_text` list corresponds to the desired output.