```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ''),) for _ in '()]' ]):
        nest_level = 1
        while opening != closing:
            if opening == ')':
                nest_level += 1
            elif closing == '(':
                nest_level -= 1
            opening = closing
        result.append(nest_level)
    return result
```

This problem can be solved by iterating through each group of parentheses, incrementing the `nest_level` variable whenever we encounter an opening parenthesis, and decrementing it whenever we encounter a closing parenthesis. The achieved `nest_level` value for each group represents the deepest level of nesting of parentheses.