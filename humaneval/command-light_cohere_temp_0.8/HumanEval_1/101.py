Here is a Python script with a self-contained function that solves the problem of separating nested parentheses into individual groups:
```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings.
    """
    unsplit and capitalize the balanced parentheses.
    e.g., ((())) ->
    balanced, will return 'Parentheses'
    """
    import re
    # Remove all non-parentheses and spaces from string
    r = re.sub(r'() &r" ",", s)
    # Capitalize first and last character of each string
    r = r.capitalize() +r
   
    # Split the string into individual groups of parentheses
    return [r.split("()")]
```
This script defines a function called `separate_paren_groups`, which takes a string as input and returns a list of strings, each representing a group of parentheses. The function uses the regex `r` to remove all non-parentheses and spaces from the string, then uses the `capitalize` method to capitalize the first and last character of each string.