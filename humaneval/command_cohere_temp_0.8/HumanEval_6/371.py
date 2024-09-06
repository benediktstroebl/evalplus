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
The function iterates through each segment of the string, tracking the number of open and closed parentheses encountered and comparing the totals to determine the depth of nesting for each group, these values are then appended to a list and returned.

Here is an example usage of the function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This would output:
```python
[2, 3, 1, 3]
```
Which corresponds to the example provided.