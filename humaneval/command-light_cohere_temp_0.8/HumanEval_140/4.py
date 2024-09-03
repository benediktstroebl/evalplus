Here's a self-contained Python script that solves the problem of markdown code alignment:
```python
def fix_spaces(text):
    """
    Replace all spaces with underscores, and handle consecutive spaces by - . 
    Returns: String with fixed spaces.
    """
    string.
    if len(text) < 2:
        return text
    new_text = ""
    for i in range(0, len(text)):
        if text[i] == ' ':
            if i > 1:  # if 2 or more spaces are consecutively
                new_text += '- '
            else:  # only 1 space
                new_text += ' '
        else:
            new_text += text[i]
    return new_text
```