```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nesting = 0
        level = 0
        for char in chunk:
            if char == '(':
                nesting += 1
            else:
                nesting -= 1
            level = max(level, nesting)
        result.append(level)
    return result
```

This script divides the input string s into multiple chunks based on spaces, and for each chunk, it counts the deepest level of nesting of parentheses. The maximum nesting level is maintained throughout the iteration and finally recorded in the result list.

Here is an example usage of the function run on the example provided in the prompt:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 

This output demonstrates the correct parsing of the nested parentheses in the provided example, with each value in the list representing the maximum nesting level for each group of parentheses.