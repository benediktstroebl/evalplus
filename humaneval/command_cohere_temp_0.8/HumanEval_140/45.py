```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The code uses a for loop to iterate through each character in the `text` string. When it encounters a space, it checks the previous character; if it was also a space, it means there are more than two consecutive spaces, so it replaces the spaces with a '-'. Otherwise, it replaces the space with an underscore. All other characters are appended as is to the `new_text` list, and then joined back to a string to return the final result. 

The problem statement mentions basic test cases, and the code has been designed to pass those basic tests.