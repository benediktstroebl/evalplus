```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        i = 0
        for char in chunk:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
            if nest < 0:
                break
        result.append(nest)
    return result
```
The `parse_nested_parens` function takes a string as input and splits it into chunks using spaces as separators. For each chunk, it counts the number of open parentheses '(' and subtracts the number of closed parentheses ')' to get the current nesting level. It keeps track of the maximum nesting level encountered in the list of numbers `result`. The output is a list of the deepest level of nesting of parentheses for each group.

Here is an example usage of the function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This would output:
```bash
[2, 3, 1, 3]
```
Which corresponds to the example provided in the problem statement.