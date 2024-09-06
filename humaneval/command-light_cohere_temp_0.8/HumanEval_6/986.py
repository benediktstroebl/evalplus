```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for match in parentheses_string. GRO.split(" ")") :
        match = match.split("()")
    match_group = [int(c) for c in match]
    if match_group:  # push first match onto stack
        stack.append(match_group)
    if match_group[0] == ():
        stack.append(match_group[1:])
    while stack:
        level = len(stack)
        for i in range(level):
            if stack[i] is ():
                stack.pop()
                else:
                    result.append(stack[i)
    return result
```

This script defines a function parse_nested_parens that takes a string of parentheses as input and returns a list of their deepest nesting levels. The function uses a opening and closing parentheses to match against a pattern, and then uses a stack to keep track of opening parentheses. The function returns the results in descending order of nesting.