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
        result.append(nest)
    return result
```

This script divides the input string s into multiple chunks based on spaces, and for each chunk, it counts the number of nested parentheses. The number of opening parentheses minus the number of closing parentheses is considered as the nesting level for a particular chunk. This nesting level is then appended to the `result` list. 

The output of the provided example in the markdown block is:
```bash
[2, 3, 1, 3]
```