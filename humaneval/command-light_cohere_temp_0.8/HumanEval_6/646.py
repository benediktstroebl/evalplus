```python
def parse_nested_parens(s: str) -> List[int]:
    """
    Recursive function to parse nested parentheses.
    Returns a all depths of nesting.
    """ s: str
    """
    group: List[int]
    """
    if not s:
        return []

    stack: List[int] = []

    for char in s:
        if char == '(':
            stack.append(0)
        elif char == ')':
            stack.pop()
            if stack[0] == None:
                return []
            group = stack.pop() + 1
            return group
        elif char == '(':
            stack.append(1)
        else:
                stack.append(char)

    return []
```

This function takes a string `s` as input, which represents multiple groups of nested parentheses separated by spaces. It returns a list of integers representing the deepest level of nesting. The function uses a stack to keep track of the opening parentheses and uses the stack to determine the correct order of closing parentheses. 

Would you like assistance with another Python problem?