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

The code uses a simple loop to build a new string with the corrected punctuation. It checks whether the character is a space and if the last added character to the new text was not an `-` (to ensure we don't want to add another - in succession). If those conditions are fulfilled, it appends an `_` sign, otherwise it adds the current character as is. 

The resulting string new_text is then joined together using ''.join(new_text) to form the final string with the spaces and double spaces replaced as described in the problem statement. 

This approach results in a clean and straightforward solution.