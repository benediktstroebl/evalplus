```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers, where each integer represents the deepest level of nesting for the corresponding group of parentheses.
    """
    def count_parens(s: str) -> int:
        # Initialize counters for open and close parentheses
        open_count = 0
        max_count = 0

        # Iterate over the string
        for char in s:
            # If the character is an open parenthesis, increment the open counter
            if char == '(':
                open_count += 1
                # Update the max counter if necessary
                max_count = max(max_count, open_count)
            # If the character is a close parenthesis, decrement the open counter
            elif char == ')':
                open_count -= 1

        # Return the maximum count of open parentheses
        return max_count

    # Split the input string into groups and map each group to its maximum nesting level
    return list(map(count_parens, paren_string.split()))

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and then calculates the maximum nesting level for each group using a helper function `count_parens`. The result is a list of integers representing the maximum nesting levels for each group.

The `count_parens` function iterates over the string, incrementing a counter for open parentheses and decrementing it for close parentheses. The maximum count of open parentheses at any point in the string is the maximum nesting level.

The example usage demonstrates how to call `parse_nested_parens` with a sample input string.