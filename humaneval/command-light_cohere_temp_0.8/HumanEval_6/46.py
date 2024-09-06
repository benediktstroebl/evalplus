```python
def parse_nested_parens(s: str) -> List[int]:
    """
    Recursively parses and returns the deepest level of nesting of parentheses in the input string.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack: List[int] = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if len(stack) == 0:
                stack.append(0)
            else:
                stack.pop()
       result = stack.pop()
    result = stack.append(1)
   return
    return result
```