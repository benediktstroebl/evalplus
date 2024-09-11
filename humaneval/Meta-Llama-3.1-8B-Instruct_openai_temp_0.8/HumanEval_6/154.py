```markdown
### Parsing Nested Parentheses
#### Problem Description
Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.

#### Solution
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string containing nested parentheses and calculate the deepest level of nesting for each group.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """Calculate the maximum depth of a string containing nested parentheses."""
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and calculate the maximum depth for each group
    return [max_depth(group) for group in paren_string.split()]

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
#### Explanation
This solution uses a helper function `max_depth` to calculate the maximum depth of a string containing nested parentheses. It iterates through the string, incrementing the depth when encountering an open parenthesis and decrementing when encountering a close parenthesis. The maximum depth encountered is returned.

The main function `parse_nested_parens` splits the input string into groups using the `split` method and applies the `max_depth` function to each group using a list comprehension. The results are returned as a list.

This solution has a time complexity of O(n), where n is the total number of characters in the input string, since it only needs to iterate through each string once to calculate the maximum depth. The space complexity is also O(n) due to the storage required for the input string and the output list.