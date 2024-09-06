```python
def fix_spaces(text):
    new_text = []
    for char in text:
        if char == ' ':
            if len(new_text) == 0 or new_text[-1] != '-':
                new_text.append('_')
            else:
                new_text.append(char)
        else:
            new_text.append(char)
    return ''.join(new_text)
```

The function `fix_spaces()` iterates through each character in the input `text`. When it encounters a space, it checks the previous character; if it's not an `-` (meaning more than 2 consecutive spaces), it replaces the space with an `_`. Otherwise, it keeps the space. This ensures that spaces are replaced with `_` except for spaces preceded by more than one `-` which all get consolidated into a single -. 

The resulting markdown code block will be:
```python
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

```