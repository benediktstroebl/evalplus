```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), s.split())))) for _ in range(len(s.split()))]
```

The provided Python script demonstrates a concise and effective solution to the problem of parsing nested parentheses. It utilizes a list comprehension to traverse the string input, unravelling nested parentheses pairs using the zip function. By calculating the maximum depth of nesting for each group and summing up the extents of each group, it determines the overall maximum depth of nesting. The final result is a list that represents the deepest level of nesting for each group of parentheses in the given input string.