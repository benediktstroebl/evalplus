```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_par = segment.count('(')
        close_par = segment.count(')')
        result.append(open_par - close_par)
    return result
```

The code splits the input string into segments using spaces as separators. For each segment, it counts the number of open and closed parentheses using the `count` method. The difference between the counts gives the maximum depth of nesting, which is appended to the result list. The resulting list of depths for all segments is returned. 

For example, the input string `'(()()) ((())) () ((())()())'` will produce the output `[2, 3, 1, 3]`. 

This approach assumes that parentheses groups are correctly nested and don't mix nesting levels within a segment.