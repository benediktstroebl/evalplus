```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group), [])))) for group in s.split(' ')]
```

The logic of the function is to split the string into different groups of parentheses, convert each group into integers that represent the level of nesting, sum these integers to combine the levels of nesting for each group, and then find the maximum nesting level by counting these levels in reverse.