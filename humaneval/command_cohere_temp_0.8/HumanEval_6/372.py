```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:]))), [])))) for x in s.split()]
```

The provided Python script demonstrates a concise and functional approach to solving the problem of parsing nested parentheses. It utilizes a list comprehension to traverse each individual group of parentheses, computing the deepest level of nesting through reversed iteration and counting the number of parentheses pairs. The sum function then aggregates these nested levels for each group, and a final list comprehension determines the maximum depth of nesting across all groups. The function outputs these maximum depths as a list, providing an effective solution to the problem.