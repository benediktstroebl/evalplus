```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        level = 0
        unbalanced = 0
        for char in bracket_level:
            if char == '(':
                unbalanced += 1
            else:
                unbalanced -= 1
            level = max(level, unbalanced)
        result.append(level)
    return result
```

The approach involves iterating through each bracket level in the input split by spaces, and maintaining a level variable that keeps track of the maximum cumulative imbalance of parentheses. The imbalance is increased for each '(' encountered and decreased for each ')' encountered. The maximum imbalance reached is considered the nesting level for that bracket level, which is then appended to the results list. The function returns a list of these nesting levels for each respective bracket level in the input. 

Here is an example usage of the function which verifies against the provided test case:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 
This technique can be further improved by utilizing a stack to iterate through the string, where '(' and ')' are pushed and popped respectively to determine the nesting level. However, the current approach is straightforward and solves the problem effectively.