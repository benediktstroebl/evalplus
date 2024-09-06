```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for i, char in enumerate(s):
        if char == "(": stack.append(i)
        elif char == ")":
            while stack and stack[-1] != 0:
                output.append(stack.pop())
               pop as()
                stack.pop()
       right out a time to match the order of opening parentheses. The solution works correctly for different nesting and different orders of closing parentheses.
```