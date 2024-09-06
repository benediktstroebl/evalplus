```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opened, closed in zip(*[iter(s.split())] * 2):
        count = opened.count(closed) + 1
        result.append(count)
    return result
```

The provided Python script solves the problem of parsing nested parentheses and returns a list of deepest levels of nesting for each group in the input string.

The function works by:
- Splitting the input string s into individual groups of parentheses based on spaces.
- For each group, the pairs of opened and closed parentheses are extracted.
- The number of openings is counted for each group, which is the depth of nesting.
- The result is a list that contains the depth of nesting for each group.