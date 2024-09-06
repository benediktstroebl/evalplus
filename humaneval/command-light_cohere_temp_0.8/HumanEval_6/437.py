Here's a self-contained Python function that solves the problem:
```python
def parse_nested_parens(s):
    """
    This function takes a string of nested parentheses separated by spaces as input and returns the deepest level of nesting as an integer.

    >>> Example a string "(()()) ((())) () ((())()())"
    => [2, 3, 1, 3]
    """
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                level = stack.pop()
                #
                stack = []
            else:
                return None
    return max(stack) if stack else None
```

This function takes a string `s` that represents multiple groups of nested parentheses separated by spaces as input, and it returns the deepest level of nesting as an integer. The function uses a stack data structure to keep track of the current level of nesting as it parses the string. The function iterates through the string, and checks if each character is an open parenthesis '('. If it is, the function appends the current character's index to the stack. If the character is a closing parenthesis ')', the function checks if there is anything in the stack. If there is, the function pops the top element from the stack and clears the stack. If there is no element left in the stack, the function returns None.