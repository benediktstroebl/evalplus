```markdown
### Nested Parentheses Parser

This Python script defines a function to parse a string of nested parentheses and calculate the deepest level of nesting for each group.

#### Code

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of deepest levels of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_depth(parens: str) -> int:
        """Calculate the maximum depth of nesting for a string of parentheses."""
        depth = 0
        max_depth = 0
        for paren in parens:
            if paren == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif paren == ')':
                depth -= 1
        return max_depth

    groups = paren_string.split()
    result = [max_depth(group) for group in groups]
    return result

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

#### Explanation

This script uses a helper function `max_depth` to calculate the maximum depth of nesting for a given string of parentheses. It iterates through each character in the string, incrementing the depth when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. The maximum depth seen so far is updated whenever a new maximum is found.

The main function `parse_nested_parens` splits the input string into groups using spaces as separators, calculates the maximum depth of nesting for each group using the `max_depth` function, and returns the results as a list.

The example usage demonstrates how to call the `parse_nested_parens` function with a sample input string and print the result.