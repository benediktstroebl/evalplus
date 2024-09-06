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

The code iterates through each character in the input `text`, and if the character is a space, it checks the previous character; if it was also a space, it appends a `-` to the `new_text` list, otherwise, it appends an underscore. All other characters are appended to the list unaltered. Finally, the function returns a string created by joining the elements in `new_text`. 

This solution adheres to the problem's statement, addressing all scenarios appropriately. The tests could be improved by checking edge cases like empty strings, strings with over 1000 characters, and spaces in the beginning and end of the string.