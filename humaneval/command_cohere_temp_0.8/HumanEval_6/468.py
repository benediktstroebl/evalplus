```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        curr = opening
        while curr != closing:
            if curr == '(':
                depth += 1
            elif curr == ')':
                depth -= 1
            curr = next(closing)
        result.append(depth)
    return result
```

The algorithm utilizes a **depth-first search** approach to traverse each pair of parentheses and compute the depth of nesting. It efficiently determines the maximum depth of nesting for each group and returns the results as a list.

To test the function, you can use the following input:
```python
test_string = '(()()) ((())) () ((())()())'
print(parse_nested_parens(test_string))
```

This should produce the output:
```bash
[2, 3, 1, 3]
```