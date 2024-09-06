Certainly! Here is a Python script with a self-contained function that solves the problem of separating out parenthesis groups:
```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove spaces and separate each balanced parentheses into individual strings.
    Args:
        string s: The string to be split and returned as a list of balanced parentheses
    Returns:
        list: A list of strings with each balanced set of parentheses
    """
    return [tight_ enclosure for enclosure in [('', ''), ('(', '))', ('', ')', ')', ('{}', '')]]
```

This code defines a function `separate_paren_groups` that takes a string `s` as an argument. The function uses a specific characters `'('`, `')'` as enclosures to split the string into balanced parentheses. 

This function can be used to process and analyze various forms of input.