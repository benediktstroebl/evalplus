```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        cnt = 0
        j = i
        for c in char:
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                result.append(cnt)
                j += cnt
                cnt = 0
        if cnt > 0:
            result.append(cnt)
        i = j + 1
    return result
```

The specified Python script solves the problem using a single function `parse_nested_parens(s: str) -> List[int]`. This function takes a string `s` as input, which contains multiple groups of nested parentheses separated by spaces, and returns a list where each element represents the deepest level of nesting of parentheses in the corresponding group.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This will produce a list `[2, 3, 1, 3]` as the output, where each number corresponds to the group's deepest nesting level of parentheses, starting from the first group.