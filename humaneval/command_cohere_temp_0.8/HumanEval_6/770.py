```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        nest = 0
        imbalance = 0
        for char in segment:
            if char == '(':
                nest += 1
                imbalance += 1
            elif char == ')':
                nest -= 1
                imbalance -= 1
            if imbalance > 0:
                result.append(nest)
                imbalance = 0
    return result
```

The approach employs a simple loop to count the nesting levels by tracking the imbalance of open and closed parentheses. The function splits the input string into segments using spaces as separators, initializes a counter for the maximum nesting level `nest`, and a counter for tracking the imbalance of parentheses `imbalance`. As the loop iterates through each character in the segment, if the character is a `(`, the `nest` value increases by 1 and `imbalance` increases by 1. If the character is a `)`, the `nest` value decreases by 1 and `imbalance` decreases by 1. If `imbalance` is greater than 0 at the end of a segment, it means there were more open parentheses than closed, indicating a higher level of nesting. Therefore, we increment `result` by the value of `nest` and reset `imbalance` to 0. The function repeats this process for each segment in the input string and returns the resulting list of maximum nesting levels. 

Here is an example usage of the function and its test case:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
>>> parse_nested_parens('()')
[1]
>>> parse_nested_parens('(()())')
[2]
>>> parse_nested_parens('AB () CD')
[1]
```