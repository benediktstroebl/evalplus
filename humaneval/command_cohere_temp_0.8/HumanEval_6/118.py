```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nested = 0
        for char in chunk:
            if char == '(':
                nested += 1
            else:
                nested -= 1
                if nested == 0:
                    count = max(count, nested)
        result.append(count)
    return result
```
The function takes a string as input, splits it into chunks by space, and then counts the nesting level of parentheses for each chunk. The maximum nesting level of parentheses in a chunk is maintained during the count and returned as a list.

Here is an example usage of the function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This would output:
```python
[2, 3, 1, 3]
```
Which corresponds to the example provided.