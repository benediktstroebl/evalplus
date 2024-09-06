```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        if char == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(i)
                stack.append(char)
            i += 1
    else:
                stack.append(stack.pop())()
               num = stack.pop()()
               num += 1
                stack.append(char)
                i += 1
    if len(stack) > 0:
        stack.append(num)
        else:
        result.append(lenum)
    return result
```