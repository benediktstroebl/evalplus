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

The given Python script defines a function `fix_spaces` that replaces all single spaces with underscores and double spaces with a hyphen (-). The function iterates through the characters of the input `text`, using a list `new_text` to track the modified characters. When a space is encountered, the function checks the previous character; if it's also a space, a hyphen is added to `new_text`, otherwise, an underscore is added. All other characters are appended unchanged to `new_text`. The final result is returned as a string, where all spaces have been appropriately replaced according to the problem's rules.