```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes in a string of multiple groups of parentheses separated by spaces.
    The deepest level of nesting is returned.
    """
    nested parentheses in the following format:
        (())...( )(...)
    """
    # Initialize empty list to store the results
    result = []

    # Iterate through each group of parentheses
    for group in parent_string.split('(\(\)\) ' '):
        # If the group is empty, append an empty list to the result
        if not group:
            result.append([])
       
        # If the group is not empty, parse it recursively
        for each in group.
    return result


# Return the result
```
This script defines a function parse_nested_parens that takes a string of nested parentheses as input and returns the deepest level of nesting of parentheses. It uses a recursive approach with a string splitting technique to handle each group of parentheses.