```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ')((').replace('(', '(') + ')))'])]:
        nested = 0
        while opening != closing:
            opening = opening.replace('(', ''.join(map(str, range(1, nested + 2))).replace(')', '))'))
            nested += 1
        result.append(nested)
    return result
```

The solution works by turning the string into a format that guarantees that every opening parenthesis has a matching closing parenthesis, and vice versa. The deepest level of nesting of parentheses for each group is then calculated and returned as a list.