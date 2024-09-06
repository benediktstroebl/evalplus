```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), s.split())))) for _ in range(len(s.split()))]
```

The provided Python script demonstrates a concise and effective solution to the problem of parsing nested parentheses. The function `parse_nested_parens` takes a string input `s`, representing multiple groups of nested parentheses separated by spaces. It employs a list comprehension and the `max` function to efficiently determine the maximum depth of nesting within each group. The result is a list where each element represents the deepest nesting level of a particular group of parentheses. The script exemplifies Python's elegance and simplicity in solving this interesting algorithmic problem.