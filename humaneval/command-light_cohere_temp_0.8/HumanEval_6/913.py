```python
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    in_string = False
    output = []

    for char in parent_string:
        if char == "(":
            if not in_string:
                stack.append(1)
            in_string = True
        else:
            in_string = False
        continue
        if char == ")":
            if len(stack) == 0:
                in_string = False
            else:
                stack.pop()
       
                in_string = True
        else:
            in_string = False
            continue
            
    if len(stack) != 0:
        in_string = False

    return output
```