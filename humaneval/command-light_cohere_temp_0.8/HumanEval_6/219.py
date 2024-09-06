Here is a self-contained Python script that defines a function `parse_nested_parens` that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function takes a string of parentheses separated by spaces and returns the deepest level of nesting for each group.

    Parameters: 
    parenthesis_string: The input string is a list of parenthesis groups separated by spaces.

    Returns: 
    list of deepest levels of nesting for each group in the input string.
    """

    return [[level] for level in enumerate(re.sub(r'\(([P] + P[0] + ... + P[i-1])+P[i]')', ' ')], [0]
```

This function uses the regex to match each group of parentheses, and then returns a list of the deepest level of nesting for each group.