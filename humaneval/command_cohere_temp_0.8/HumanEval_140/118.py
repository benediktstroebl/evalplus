```python
def fix_spaces(text):
    new_text = []
    for char in text:
        if char == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(char)
    return ''.join(new_text)
``` 

The code uses a list to build the new string, ensuring that all spaces are correctly replaced. In the final step, the code joins the list into a string to provide the final corrected text.