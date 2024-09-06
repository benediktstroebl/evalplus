```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:]))), [])))) for _ in s.split()]
```

The provided Python script defines a function called `parse_nested_parens` that takes a string `s` as input. This string contains multiple groups of nested parentheses separated by spaces. The function returns a list where each element represents the deepest level of nesting of parentheses in its corresponding group.

The function uses a list comprehension and the `sum` function to sum over the pairs of corresponding parentheses, reversing the sum and then finding the maximum nesting level. The result is a list that accurately reflects the deepest nesting level for each group of parentheses in the input string.