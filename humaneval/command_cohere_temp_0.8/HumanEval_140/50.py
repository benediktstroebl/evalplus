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

The given Python script defines a function `fix_spaces` that takes a string `text` as input. It iterates through each character in the input text and checks if it's a space. If the current character is a space, it checks if the previous character was also a space by examining the length of the `new_text` list and the last element in the list. If the previous character was a space, it replaces the consecutive spaces with a single `-` character. Otherwise, it replaces the space with an underscore `_'. For all other characters (non-spaces), it directly appends them to the `new_text` list.

After processing all characters, the function joins the `new_text` list back into a string and returns the modified text with fixed consecutive spaces.