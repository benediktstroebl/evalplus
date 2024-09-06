```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(': stack.append(len)
        if c == ')':
            if stack:
                output.append(stack.pop()
            thenpop  then if stack == []:
                break
            stack.clear()
    } if stack:
                stack.append(None)
    return output
```

This code defines a function named `parse_nested_parens` that takes a string `s` as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. The function uses a stack to keep track of opening parentheses and appends the current group of parentheses to the `output` list when it encounters a closing parenthesis. The function iterates through the string character by character, and for each opening parenthesis `(`), it appends the current group of parentheses to the `stack` and then pops the group from the stack, appends it to the `output` list, and clears the stack. This process continues until the  a closing parenthesis is encountered, at which point the function returns the `output` list, which contains the deepest level of nesting of parentheses in the original string.