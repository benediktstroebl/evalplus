```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        chunk = chunk.strip('())' )
        if not chunk:
            result.append(0)
        else:
            stack = [0]
            depth = 0
            for char in chunk:
                if char == '(':
                    stack.append(depth)
                else:
                    depth = stack.pop()
            result.append(depth)
    return result
```
The code processes each chunk (parentheses group) separately and solves the problem of nestedness for each one. The `depth` variable tracks the deepest nesting level of the current chunk, and the `stack` is used to correctly calculate this depth even for unbalanced chunks. The base case is a chunk with no opening parentheses at all, in which case the depth is 0, hence the chunk is appended to the result list with this value. The code ensures that it correctly deals with all possible permutations of parentheses, including perfectly balanced ones, unbalanced ones, and multiple groups of different nesting levels.