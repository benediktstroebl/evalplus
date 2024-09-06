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

The code uses a list (`new_text`) to build the new string, `''.join(new_text)`-, which avoids problems with overlapping strings and makes sure the strings are 'str' and not 'bytes'. It also uses a conditional to deal with replacing consecutive spaces with a single - .