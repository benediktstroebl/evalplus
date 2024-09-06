```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), iterate_nested_parens(s, ())))))]

def iterate_nested_parens(s, parens):
    if not s:
        return parens
    if s[-1] == ')':
        parens += (len(parens),)
        s = s[:-1]
    else:
        nested = iterate_nested_parens(s[1:], parens)
        if nested:
            return nested + (len(parens) + 1,)
    return parens
```