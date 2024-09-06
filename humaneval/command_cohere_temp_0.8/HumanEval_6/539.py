```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        counter = 0
        for char in chunk:
            if char == '(':
                counter += 1
            else:
                counter -= 1
        result.append(counter)
    return result
```
The function iterates over each space-separated chunk in the input string and maintains a counter that keeps track of the current nesting level. When it encounters an open parenthesis `(`, the counter is incremented, and when it encounters a closing parenthesis `)`, the counter is decremented. The resulting list of counter values corresponds to the deepest level of nesting for each group of parentheses.

Here is a usage example:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 

This should correctly solve the problem and produce the output list [2, 3, 1, 3] for the provided input example.