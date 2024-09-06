Here is a Python script that includes a self-contained function `parse_nested_parens` that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes in a string of nested parentheses separated by spaces, and returns a list of the deepest levels of nesting.
    Args:
    s (string): A string of nested parentheses separated by spaces.
    Returns:
    list of the deepest level of nesting for each group of parentheses.
    """

return [match.degreelargest_level(s[i:]) for i in range(len(s))]]
def match_largest_level(match):
    """
    This function takes in a match object returned by the match() function, 
    and returns the largest level of nesting.
    Args:
    match (match): match object returned by the match() function.
    Returns:
    int: the largest level of nesting of the matched parentheses.
    """

return max(match.levellargest_level(match), match.largestlargest_level(match[0]))
```
This function uses the `match()` function to match each group of parentheses, and uses the `largest_level()` function to get the largest level of nesting for each match.  The `parse_nested_parens()` function then returns a list of the deepest level of nesting for each group of parentheses.