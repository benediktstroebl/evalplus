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

The code block defines a Python function called `fix_spaces` that takes a string text as input. Within the function, a new text list is initialized to store the modified characters. It iterates through each character in the input `text`. If the character is a space, it checks the previous and next characters in the `new_text` list, ensuring that consecutive spaces are replaced with a single - character. The resulting modified string is returned.