```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group of parentheses.
    """

    def count_levels(s: str) -> int:
        """
        Helper function to count the deepest level of nesting of parentheses in a string.
        """
        level = 0
        max_level = 0
        for char in s:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        return max_level

    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group and count the deepest level of nesting
    for group in groups:
        results.append(count_levels(group))
    
    return results

# Example usage:
paren_string = '(()()) ((())) () ((())()())'
print(parse_nested_parens(paren_string))  # Output: [2, 3, 1, 3]
```