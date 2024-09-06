```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        depth = 0
        level = 0
        for char in chunk:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
            depth = max(depth, level)
        result.append(depth)
    return result
```

The `parse_nested_parens` function takes a string as input and returns a list of the deepest levels of nesting of parentheses in each nested group. It splits the input string into chunks by spaces, and then iterates through each character in the chunk, maintaining a `depth` that keeps track of the maximum nesting level encountered so far and a `level` that keeps track of the current nesting level. It increments the `level` for each opening parenthesis and decrements it for each closing parenthesis. The maximum nesting level is recorded in the `result` list for each group.

Here is an example usage of the function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This will output:
```bash
[2, 3, 1, 3]
```

The function accurately extracts the depth of nesting for each group of parentheses in the provided test case.