```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate groups of parentheses into separate strings.
    Returns a
    balanced (each open brace is properly closed) and not nested within each other.
    """
    
    :type: str
    """
    return [parent.strip(s) for parent in parentheses.strip(" ")]
```
The function, `separate_paren_groups`, takes a string of parentheses as input and returns a list of strings, each containing a balanced group of parentheses. The function works by iterating over each parenthesis string in the input and transforming it into a balanced string of parentheses.