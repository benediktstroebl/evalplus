```python
def parse_nested_parens(s: str) -> List[int]:
    """
    A utility function to parse nested parentheses.
    Args:
        string s: string with nested parentheses
    Returns:
        list of indices representing the deepest nesting level of each group of parentheses.
    """
    group, is the innermost level of the innermost pair of parentheses.
    """ example:
    Input: ('(()())((()))()())')
    Output: [2, 3, 1, 3]
    """
    stack: List[int] = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        if char == ')':
                if len(stack) == 0:
                    stack.pop()
                if len(stack) > 1:
                    stack.append(len)
                else:
                    break
    return stack
```