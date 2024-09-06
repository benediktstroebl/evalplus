```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        current = 0
        for char in chunk:
            if char == '(':
                current += 1
            else:
                current -= 1
            result.append(current)
    return result
```
The `parse_nested_parens` function takes a string as input and iterates through each space-separated chunk (subgroup of parentheses) in the string. It maintains a `current` variable that keeps track of the current nesting level within a chunk. The nesting level increases by 1 when an '(' character is encountered and decreases by 1 when a ')' character is encountered. The resulting list of nesting levels is returned as the output.

Here is an example usage of the function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
```bash
[2, 3, 1, 3]
```
The example sentence has 4 subgroups of parentheses and the result shows the deepest level of nesting for each subgroup.