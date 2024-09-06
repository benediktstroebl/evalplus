Here is a self-contained Python script that solves the problem of nested parentheses parsing:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of multiple groups of parentheses separated by spaces as input.
    It returns a levels of nesting, with the innermost nesting having the deepest level.
    """
    example usage:
    [2, 3, 1, 3] = parse_nested_parens('(()()) ((())) () ((()))()())')
    """
    def helper(match):
        if len(match) == 1:  # if the match is a single character
            return len(match)
        else:
            # if the match is a group of two or more characters, return the depth of nesting
            return helper(match[0]) + 1
    return helper(s)

return [helper(s) for s in parse_nested_parens('(()()) ((())) () ((()))()())')]
```
This script defines a helper function that recursively traverses the string and returns the depth of nesting for each group of parentheses. The main function then loops through each group of parentheses in the string and calls the helper function for each group, keeping track of the deepest level of nesting. 

It uses the typing module for better code readability and function definition.