```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group))))) for group in s.split(' ')]
```

The logic of the function is to split the string into different groups of parentheses, convert each group into integers that represent the level of nesting, add up those integers to aggregate levels of all nests in a group, and find the maximum level of nesting by taking the maximum level of aggregation for each group.