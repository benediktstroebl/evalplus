```python
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with nested parentheses into a list of their depths.
    Args:
    s (str) containing one or more groups of parentheses.
    Returns:
    A list of depths of each group of parentheses in order of appearance.
    """ Example to test this function is a string containing one or more groups of parentheses separated by spaces.
    """
    expected to be a string representation of multiple groups for nested parentheses.

    Returns: list of integer depths of each group of parentheses in order of appearance.
    """
    example:
    >>> parse_nested_parens('(()()) ((())) () ((()))()')
    [2, 3, 1, 3]
    """
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(1)
        else:
            if stack:
                result.append(stack.pop(). stack.pop()
                stack.pop() = the Region of an closing parenthesis is the same as the opening parenthesis. This ensures the correct tracking of nesting levels.
    return result
```