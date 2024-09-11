```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]

    :param paren_string: A string containing multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting of parentheses for each group.
    """
    def max_depth(s: str) -> int:
        """
        Helper function to calculate the maximum depth of nesting for a given string of parentheses.

        :param s: A string of parentheses.
        :return: The maximum depth of nesting.
        """
        stack = 0
        max_stack = 0
        for char in s:
            if char == '(':
                stack += 1
                max_stack = max(max_stack, stack)
            elif char == ')':
                stack -= 1
        return max_stack

    # Split the input string into groups of parentheses
    groups = paren_string.split()
    # Initialize an empty list to store the results
    results = []
    # Iterate over each group and calculate the maximum depth of nesting
    for group in groups:
        results.append(max_depth(group))
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and for each group, calculates the maximum depth of nesting using a helper function `max_depth`. The function then returns a list of integers representing the maximum depth of nesting for each group. The script includes a test case to demonstrate the function's correctness.