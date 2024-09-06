```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(len, group.split())))) for group in s.split(' ')]
```

The logic of the `parse_nested_parens` function is to split the input string s into multiple groups separated by spaces, calculate the length of each group (considered as a list of strings), and then use `max` with a conditional statement to calculate the deepest level of nesting of parentheses for each group. Finally, the results for each group are returned as a list.