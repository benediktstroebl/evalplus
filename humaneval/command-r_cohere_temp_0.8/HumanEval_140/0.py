```python
def fix_spaces(text):
    """
    Replaces all spaces in the input string with underscores, and if there are more than 2 
    consecutive spaces, replaces them with a dash -.
    """
    import re

    return re.sub(" +", "-", text.replace(" ", "_"))
```