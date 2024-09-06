```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', '))').enumerate()]):
        depth = opening
        while closing != len(s) and s[closing] == '(':
            depth += 1
            closing += 1
        result.append(depth)
    return result
```
This Python script defines a list comprehension that extracts all nested parentheses from the input string and calculates their deepest level of nesting. The `result` variable stores these depths, and the final list is returned.