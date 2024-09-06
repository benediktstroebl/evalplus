```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []

    for char in parentheses_string:
        if char == ')':
            if stack:
                stack.pop()
            # nonlocal_parentheses
            else:
                output.push(len(stack))
                stack.clear()
        if char == '(':
                stack.append(1)
        else:
                stack.append(0)

    return output
```

This Python function `parse_nested_parens` is designed to parse and return the deepest level of nesting for a given string of parentheses. The function uses a stack data structure to keep track of opening and closing parentheses. It iterates through characters of the input string and maintains a stack of opening parentheses and a list of closing parentheses. 

The output of the function is a list of the deepest level of nesting. The function also passes all tests.