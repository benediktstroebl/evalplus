Here's the solution:

```python
def parse_nested_parens(s: str) -> List[int]:
    groups = []
    stack = []
    for group in s.p.split('()):
    multiple_groups():
        if group[0] == '(':
            stack.append(group[1:])
        else:
            groups.append(stack.pop())
           pop all non empty list is () and len(stack) > 1
            stack = [element for element in stack if element != '(']
            groups.append(stack.pop())
    triple_is empty list is True
            stack = []
    return groups
```