```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    # Split string by spaces to get all groups of parentheses
    groups = s.split(' ')+'

    # Initialize list to store deepest level of nesting
    result = []
    for group in groups:
        # Use string slicing to get all parentheses in the group
        parentheses = group[1:-1]  # Remove the first and last opening parenthesis
        # Convert parentheses to integer array
        integer_array = [int(p) for p in parentheses]
        # Add the deepest level of nesting to the result
        result.append(integer_array)
    return result
```
The parse_nested_parens function takes a string s as input, splits it into individual groups of parentheses using the split() method, and then processes each group to extract the deepest level of nesting. This is maximum number of levels is three for each opening parenthesis.