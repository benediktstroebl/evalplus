Here is a Python script that uses a stack data structure to solve the problem:
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    :param paren_string: A string of groups separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
    """
    def calculate_depth(paren_group: str) -> int:
        """Calculate the deepest level of nesting for a single group."""
        depth = 0
        max_depth = 0
        for char in paren_group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and calculate the depth of each
    groups = paren_string.split()
    return [calculate_depth(group) for group in groups]

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This script defines a helper function `calculate_depth` to calculate the deepest level of nesting for a single group of parentheses. It then uses this function to calculate the depth of each group in the input string and returns the result as a list.