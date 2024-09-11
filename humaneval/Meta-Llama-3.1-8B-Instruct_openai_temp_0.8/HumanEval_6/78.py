```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting for each group.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.
    """

    def max_nesting(group: str) -> int:
        """
        This is a helper function to find the maximum nesting level of a single group of nested parentheses.
        It uses a stack to keep track of the opening parentheses and counts the number of closing parentheses
        that are unmatched because their corresponding opening parentheses have been closed.

        Args:
            group (str): A string of nested parentheses.

        Returns:
            int: The maximum nesting level of the group.
        """
        stack = []
        max_level = 0
        level = 0
        for paren in group:
            if paren == '(':
                stack.append(paren)
                level += 1
                max_level = max(max_level, level)
            elif paren == ')':
                if stack:
                    stack.pop()
                    level -= 1
                else:
                    level += 1
        return max_level

    # Split the input string into groups and calculate the maximum nesting level for each group
    return [max_nesting(group) for group in paren_string.split()]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses separated by spaces and returns a list of the deepest level of nesting for each group. It uses a helper function `max_nesting` to find the maximum nesting level of a single group of nested parentheses. The function splits the input string into groups, calculates the maximum nesting level for each group using the `max_nesting` function, and returns the list of results.