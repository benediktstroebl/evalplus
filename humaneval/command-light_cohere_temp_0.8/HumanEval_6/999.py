```python
def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    result = []

    for char in paren_string:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if not stack or stack[-1] == 1:
                result.append(0)
            stack.append(0)
        elif stack and stack[-1] == 2:
                result.append(stack.pop())
                if char == ")":
                stack.append(1)
            else:
                stack.append(0)

    return result
```

This function parses a string of nested parentheses and returns the deepest level of nesting for each group of parentheses. It uses a stack to keep track of the nesting level of each group of parentheses. The function works by iterating through each character in the string and following the appropriate rules.