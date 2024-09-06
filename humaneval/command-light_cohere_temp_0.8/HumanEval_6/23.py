```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []

    for char in parenthes_string:
        if char == ')':
            stack.append(len)
        if char == '(':
            stack.append(0)
        else:
            stack.append(stack.pop())
            max_nesting = 3
            while len(stack) > max_nesting:
                stack.pop()
            result.append(stack.pop())
           return result
return result
```
This function parses a string of nested parentheses, and returns the deepest level of nesting. The function uses a stack data structure to keep track of the open parentheses and closed parentheses, and the result list to store the deepest level of nesting found.