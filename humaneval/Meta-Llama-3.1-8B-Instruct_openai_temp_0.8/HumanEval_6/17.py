```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input.
    It returns a list of the deepest level of nesting for each group of parentheses.

    :param paren_string: A string of nested parentheses separated by spaces
    :return: A list of the deepest level of nesting for each group of parentheses
    """
    def max_depth(s: str) -> int:
        """
        This function calculates the deepest level of nesting for a given string of parentheses.

        :param s: A string of parentheses
        :return: The deepest level of nesting
        """
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups of parentheses
    groups = paren_string.split()
    # Calculate the deepest level of nesting for each group and return the results
    return [max_depth(group) for group in groups]

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
# Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group of parentheses. The function uses a helper function `max_depth` to calculate the deepest level of nesting for a given string of parentheses. The `max_depth` function iterates over the string, incrementing a depth counter when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. The maximum depth encountered is returned as the result. The `parse_nested_parens` function splits the input string into groups of parentheses, calculates the deepest level of nesting for each group using `max_depth`, and returns the results as a list.