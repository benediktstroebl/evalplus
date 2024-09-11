```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group.
    """
    def max_depth(substring: str) -> int:
        """ Recursively calculates the deepest level of nesting for a substring. """
        max_level = 0
        current_level = 0
        for char in substring:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                if current_level == 0:
                    raise ValueError("Unbalanced parentheses in substring")
                current_level -= 1
        if current_level!= 0:
            raise ValueError("Unbalanced parentheses in substring")
        return max_level

    # Split the input string into substrings by spaces and calculate the maximum depth of each substring
    return [max_depth(substring) for substring in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `max_depth` to calculate the deepest level of nesting for a substring. The `parse_nested_parens` function splits the input string into substrings by spaces and applies `max_depth` to each substring. It uses a list comprehension to efficiently calculate the maximum depths for all substrings and returns the result.