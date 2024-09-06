```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        nest = 0
        found = 0
        while opening != closing:
            if opening == '(':
                nest += 1
                opening = closing
                found += 1
            elif closing == ')':
                nest -= 1
                closing = opening
                found += 1
            if nest > depth:
                depth = nest
        result.append(found)
    return result
```

The provided Python script solves the problem of parsing nested parentheses and returns the deepest level of nesting for each group in the input string separated by spaces.

The function employs a simple loop structure to monitor the "balance" of opening and closing parentheses, incrementing the `depth` if the nesting exceeds the previous highest level. The final result is a list containing the determined deepest nesting level for each corresponding group in the input string.