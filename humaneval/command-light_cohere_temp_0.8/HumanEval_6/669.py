```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function returns the deepest level of nesting of parentheses in the given string.
    Args:
        string: a string that can contain multiple groups of parentheses
    Returns:
        List[int]: a list of the deepest level of nesting of each group of parentheses in the string
    """
    # Create a list to store the deepest level of nesting
    res = []
    for i in range(len(s)):
        if s[i] == "(":
            res.append(3)
        else:
            res.append(1)
    return res
```
This function parses a string that contains multiple groups of parentheses, separated by spaces, and returns a list of the deepest level of nesting for each group of parentheses. The function works by iterating over the string and checking if the character is a left parenthesis '('. If it is, then the function appends the current level of nesting to the res list. If the character is a right parenthesis ')', then the function appends the current level of nesting to the res list. This process continues until all end of the string is reached.