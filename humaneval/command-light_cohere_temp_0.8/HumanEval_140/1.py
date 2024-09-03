```python
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    Returns: string with fixed spaces
    """
    text = text.replace(' ', '_')
    if ' ' in text and len(text.find(' ')) > 2 else text
    
    return text
```