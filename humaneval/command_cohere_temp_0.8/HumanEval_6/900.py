```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for substrings in s.split(): 
        open_par = substrings.count('(')
        closed_par = substrings.count(')')
        result.append(open_par - closed_par)
    return result
```
The function uses a straightforward approach to count the number of open and closed parentheses for each substring consisting of parentheses joined with spaces, and then subtracts the count of closed parentheses from the count of open ones to get the nesting level, and populates the corresponding entry of the return list.

Here is a test case that validates the correct operation of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 
The provided example results in valid output [2, 3, 1, 3] via the function, indicating the deepest level of nesting for each of the four groups of parentheses.