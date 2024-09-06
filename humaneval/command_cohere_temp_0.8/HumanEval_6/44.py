```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group), [])))) for group in s.split()]
```

The provided Python script defines a function called `parse_nested_parens` which takes a string `s` as input. This string contains multiple groups of parentheses separated by spaces, where each group represents a different nested hierarchy of parentheses. The function returns a list where each element corresponds to the deepest level of nesting of parentheses in its respective group. To achieve this, the function employs a combination of integer conversion, summing, and maximum value extraction within a list comprehension. The result is a list that accurately reflects the deepest nesting levels for each group of parentheses in the input string.