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

The function iterates through the input text, and for each character, it checks if it is a space. If it is, it checks if the last two characters in the `new_text` list are also spaces, implying that there are more than two consecutive spaces. If this condition is true, it replaces the current space with a `-`, otherwise, it replaces the current space with an `_`. If the character is not a space, it is added to the `new_text` list as is. Finally, the function joins the list of new characters back into a string and returns the result. 

This solution is efficient and can solve the given problem in different scenarios.