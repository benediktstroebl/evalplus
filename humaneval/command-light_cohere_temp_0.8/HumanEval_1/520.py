```python
def separate_paren_groups(s): 
    result = []
    stack = []
    for c in s: 
        if c == '(': 
            stack.append(c)
        else: 
            if not stack or stack[-1] == '(':
                result.append(c)
                stack.append(')')
            if stack[-1] == ')':
                stack.pop()
    if c == ' ':
                stack.append(c)
            else: stack.append(c)
    return result
```
This code defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated parenthesis groups. The function uses a stack to keep track of open parentheses and iterates through the input string, adding characters to the stack and appending corresponding closed parentheses when appropriate. The function returns the process by either adding the closing parenthesis to the stack or adding a space if it is missing.