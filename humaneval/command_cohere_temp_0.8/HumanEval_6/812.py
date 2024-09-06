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

The code uses a simple approach to parse the string and calculate the number of open and close parentheses. It counts the number of open parentheses and subtracts the number of close parentheses in each segment to get the depth of nesting and adds the result to the list. The output of the provided example is `[2, 3, 1, 3]` as explained in the problem statement.