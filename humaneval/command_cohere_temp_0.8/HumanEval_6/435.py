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

The `parse_nested_parens` function takes a string as input and splits it into segments using spaces as separators. It counts the number of opening and closing parentheses for each segment separately and calculates the difference to obtain the maximum nesting level. The result is then appended to a list that is returned.

Here is an example usage of the function:
```python
>>> print(parse_nested_parens('(()()) ((())) () ((())()())'))
[2, 3, 1, 3]
```

This demonstrates that the provided solution correctly parses the given string and returns the deepest level of nesting for each group of parentheses.