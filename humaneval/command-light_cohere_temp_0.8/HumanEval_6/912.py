```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []

    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if stack:
                result.append(stack.pop())
           
        stack.pop(), stack.append(0)
        return result
```

This Python script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest nesting levels. The function uses a stack data structure to keep track of the current nesting level. It iterates through nested parentheses and pushes the level onto the stack when it encounters '(', and populates the result list with the values from the stack when it encounters the ')' character.