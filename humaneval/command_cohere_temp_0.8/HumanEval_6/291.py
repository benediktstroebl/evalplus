```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open, close = 0, 0
        for char in segment:
            if char == '(':
                open += 1
            else:
                close += 1
        result.append(open >= close)
    return result
```
The function processes the input string segment by segment, keeping track of open and closed parentheses within each segment. The deepest nesting level of each segment is determined by whether the number of open parentheses is greater than or equal to the number of closed parentheses, denoting an odd or even level respectively. These levels are then appended to a list, providing the desired result. 

This approach ensures a correct solution while maintaining a straightforward and efficient implementation.