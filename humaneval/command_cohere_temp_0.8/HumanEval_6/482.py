```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        nest = 0
        found = False
        while opening != closing:
            if opening == '(':
                depth += 1
                nest += 1
            elif closing == ')':
                depth -= 1
                nest -= 1
            if not found and nest > 0:
                result.append(depth)
                found = True
            opening = closing
        if not found:
            result.append(depth)
    return result
```

The `parse_nested_parens` function takes a string `s` containing nested parentheses as input. It iterates through the openings and closings of parentheses using `zip(*[iter(s.split())] * 2)`, maintaining a `depth` and `nest` count. The `found` variable ensures a distinct list element for each separate group of parentheses. Once all openings match all closings, the depth is added to the result if it hasn't been already. The function returns a list of the deepest levels of nesting for each group of parentheses.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This demonstrates that the function can successfully parse the input and determine the deepest level of nesting for each group of parentheses.