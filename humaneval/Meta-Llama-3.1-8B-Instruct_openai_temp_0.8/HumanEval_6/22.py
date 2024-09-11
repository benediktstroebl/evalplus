```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of deepest levels of nesting for each group of parentheses.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_depth(s: str) -> int:
        # Initialize the depth and max depth counters
        depth = 0
        max_depth = 0
        for char in s:
            # If the character is an opening parenthesis, increment the depth
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            # If the character is a closing parenthesis, decrement the depth
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and count the depth of each group
    return [count_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses. It uses a helper function `count_depth` to count the depth of a single group of parentheses. The `count_depth` function uses a simple loop to iterate over the characters in the group, incrementing a depth counter when it encounters an opening parenthesis and decrementing it when it encounters a closing parenthesis. It keeps track of the maximum depth seen so far and returns this value at the end. The main function splits the input string into groups and applies `count_depth` to each group to produce the output list.