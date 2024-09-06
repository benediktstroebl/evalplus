```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), s.split())))) for _ in range(len(s.split()))]
```

The provided code works as follows:
- The code takes a string `s` as input, where `s` is a string represented multiple groups for nested parentheses separated by spaces.
- It uses `zip` to combine each pair of parentheses into a tuple, and `map` to transform each string of parentheses into a list of tuples.
- Subsequently, it uses `sum` to combine the list of tuples into a single tuple, and `reversed` to reverse the tuple to keep the deepest pair of parentheses at the first element.
- Finally, it uses `max` to find the maximum value (deepest level of nesting) for each group of parentheses.