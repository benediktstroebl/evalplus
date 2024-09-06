```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for substrings in s.split(' '): 
        open_par = substrings.count('(')
        close_par = substrings.count(')')
        result.append(open_par - close_par)
    return result
```
The function uses a straightforward approach to count the number of openings and closings for each substring consisting of parentheses, and returns the difference which corresponds to the deepest level of nesting.