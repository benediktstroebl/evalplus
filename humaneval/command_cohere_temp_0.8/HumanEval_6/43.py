Here's a Python script with a self-contained function that solves the problem using a concise logic to determine the deepest level of nesting of parentheses for each group in the input string:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(1 + c // 8 for c in char_count(s, i)) for i, _ in enumerate(s.split())]

def char_count(s: str, c: int) -> int:
    return s.count(c) - s.count(c, c)
```

This approach uses a balanced counter approach, as explained earlier. The `char_count` function calculates the count of opening and closing parentheses to determine the depth of nesting for each group in the given input string. The `parse_nested_parens` function then uses these depth values to produce the resulting list.