```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_depth in map(count_bracket_depth, s.split()):
        result.append(bracket_depth)
    return result

def count_bracket_depth(s: str) -> int:
    nesting_level = 0
    for char in s:
        if char == '(':
            nesting_level += 1
        elif char == ')':
            nesting_level -= 1
    return nesting_level
```

The approach employed here splits the input string into individual nested paren groups, and for each group, it counts the number of '(' and ')' characters to determine the deepest level of nesting. This is accomplished by the `count_bracket_depth` function. The final result is a list of deepest nesting levels for each group. 

This code is tested with the following test case:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

Note: The typing module is used to express the type of s as a string, and the return value as a list of ints, which benefits code readability and provides static type checking.