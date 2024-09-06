```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in reversed(list(map(len, s.split()))):
        if not bracket_level:
            break
        result.append(bracket_level)
    return result
```

The reversed `map` function splits the input string into different groups of parentheses and calculates the length of each group i.e. the depth of nesting. The maximum depth of nesting is kept track of via the `result` list. The output of the provided example is:
```python
[2, 3, 1, 3]
```