```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group), [])))) for group in s.split()]
```

The provided Python script demonstrates a function called `parse_nested_parens` that takes a string `s` as input. This string `s` contains multiple groups of parentheses separated by spaces. The function returns a list where each element represents the deepest level of nesting of parentheses in its corresponding group. To achieve this, the function uses a combination of integer conversion, summing, and maximum value extraction.