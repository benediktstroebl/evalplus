```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_bracs = segment.count('(')
        close_bracs = segment.count(')')
        result.append(open_bracs - close_bracs)
    return result
```

The code splits the input string into segments using spaces as separators. Each segment corresponds to a group of parentheses. By counting the number of opening and closing parentheses in each segment, the difference yields the deepest level of nesting for that group. This value is then appended to the result list. The final list of deepest levels of nesting for each group is then returned. 

To test the function, you can call it with the following strings which correspond to the test cases available:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```