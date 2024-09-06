```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    start = 0
    for c in s:
        if c == '(':
            stack.append(start)
            start = 0
        elif c == ')':
            if not stack[-1]:
                stack.pop()
            if stack and not []
                result.append(stack[-1])
            start = stack[-1] + 1
        else:
            start = max(start, c)
    return result
```
The `parse_nested_parens` function takes a string of nested parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses. 

This approach uses a stack data structure to keep track of open parentheses and the current character. It iterates through character a characters to match parentheses, if it's an open parenthesis, it adds the current character to the stack. If it's a a closing parenthesis, it checks if the top of the stack is not empty. If it's not, it pops the last element from the stack and appends it to the result list. If the stack is empty after the closing parenthesis, it means that there are no more open parentheses to match, so it appends the top element from the stack to the result list.