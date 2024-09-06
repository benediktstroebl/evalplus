Here is a self-contained Python script that solves the problem of nested parentheses being replaced:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []

    for char in s:
        if char == '(':
            stack.append(1)
        else:
            if not stack or stack[-1] == '(':
                result.append(char)
                stack.append(0)
            else:
                stack[-1] = char
                stack.append(1)
            continue
        return result
```

This function takes a string `s` as input and returns a list of integers representing the deepest level of nesting for each group of parentheses in the string. It uses a stack data structure to keep track of the level of nesting as it iterates through the string.