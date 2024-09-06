```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:]))), [])))) for s in s.split()]
```

The provided Python script defines a function called `parse_nested_parens` which takes a string `s` as input. This string `s` contains multiple groups of nested parentheses separated by spaces. The function returns a list where each element represents the deepest level of nesting of parentheses in its corresponding group. To achieve this, the script uses a list comprehension and the `max` function to find the maximum depth of nesting among all the parentheses in each group. The results are then combined using the `sum` function and reversed to ensure they are in descending order. The list of depths is finally split using space as a delimiter into a list of integers.