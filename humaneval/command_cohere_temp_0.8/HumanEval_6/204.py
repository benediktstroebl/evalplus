```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        chunk = chunk.replace(')', '').replace('(', '')
        depth = len(chunk) if chunk else 0
        result.append(depth)
    return result
```
The function iterates over the provided string and processes each chunk (a part between two spaces) separately. The nestedness of each chunk is determined by the number of opening parentheses minus the number of closing parentheses. The result is a list that contains the depth of nesting for each chunk.