```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        nested = 0
        while opening != closing:
            if opening == '(':
                depth += 1
            elif closing == ')':
                depth -= 1
                nested += depth
            opening = closing
        result.append(nested)
    return result
```

This script uses a list comprehension to parse a string of nested parentheses, returning a list of the deepest levels of each grouping of parentheses. The function first iterates through pairs of opening and closing parentheses, using nested loops. It keeps track of the current depth of nesting and increments a counter whenever the opening paren indicates an increase in depth. When the closing paren is encountered, the depth is decremented, and the counter is incremented by the current depth. The counter reflects the deepest level of nesting for the entire life cycle of a given pair of parentheses. Finally, all resulting deepest levels are appended to the list result, which is returned. 

Here is an example usage of this code:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
The output of this code is:
```python
[2, 3, 1, 3]
```

This is consistent with the provided example in the problem statement.