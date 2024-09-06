```python
def parse_nested_parens(s):
    """
    Input to this function is a string representing multiple groups for nested parentheses separated by spaces.
    It returns a recursive list of the deepest level of nesting.
    """
    nested parens, opening parenthesis, close parenthesis, and spaces.
    Args:
        s: str, the string to parse the nested parentheses
    Returns:
    List[int], each index represents a level of nesting
    """
    def stack(char):
        if char == '(':
            return [0] + stack(')')
        elif char == ')':
            stack[-1].append(1)
            return stack(' ') + stack('()')
        else:
            stack[-1].append(char)
    return stack()
 
    stack = stack('(()()) ((())) () ((())()())')
    return stack()
  ```  This code defines a `parse_nested_parens` function that takes a string as input and returns a list of integers, with each integer representing a level of nesting.  It deepest level of nesting.