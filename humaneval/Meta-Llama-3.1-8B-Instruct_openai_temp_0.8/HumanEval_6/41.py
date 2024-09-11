```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function parses a string of nested parentheses and returns a list of the maximum nesting level for each group.

    Args:
    paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the maximum nesting level for each group.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    def count_nestings(s: str) -> int:
        """
        This function counts the maximum nesting level for a single group of parentheses.

        Args:
        s (str): A group of parentheses.

        Returns:
        int: The maximum nesting level for the group.
        """
        max_nesting = 0
        current_nesting = 0
        for char in s:
            if char == '(':
                current_nesting += 1
                max_nesting = max(max_nesting, current_nesting)
            elif char == ')':
                current_nesting -= 1
                # If the current nesting is negative, set it to 0, because we can't have negative nesting
                current_nesting = max(0, current_nesting)
        return max_nesting

    # Use a list comprehension to count the maximum nesting level for each group
    return [count_nestings(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input. It splits the string into groups of parentheses, and then uses a helper function `count_nestings` to count the maximum nesting level for each group. The `count_nestings` function iterates over the characters in the group, incrementing the current nesting level when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. The maximum nesting level is updated whenever the current nesting level exceeds the current maximum. Finally, the script tests the function with the provided example.