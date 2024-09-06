```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nest = 0
        for char in chunk:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            count = max(count, nest)
        result.append(count)
    return result
```
The code splits the input string into chunks based on spaces, and for each chunk, it keeps track of the maximum nested level of parentheses encountered. The maximum depth is maintained even if unbalanced parentheses are present in the string. The result list stores these maximum depths for each corresponding chunk.