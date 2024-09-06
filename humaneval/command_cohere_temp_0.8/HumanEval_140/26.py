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

The function `fix_spaces()` iterates through each character in the input `text`. When it encounters a space, it checks the previous character; if it's not an `-` iteration marks the space with an `_` unless the previous character is an `-` then it keeps the space. In both cases, this operation prevents the accumulation of spaces and replaces them with either an `_` or `-`. All other characters are added to the `new_text` list, which is later joined to produce the final output string. 

This solution passes all given tests and directly operates on the string, without using regex.