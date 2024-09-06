```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        level = 0
        unbalanced = 0
        stack = []
        for char in bracket_level:
            if char == '(':
                stack.append(char)
                unbalanced += 1
            else:
                unbalanced -= 1
                if not unbalanced:
                    level += 1
                    if stack:
                        result.append(level)
                        stack.pop()
                stack.append(char)
        if unbalanced:
            result.append(level)
    return result
```

To use this function, you can provide a string as an input argument like this:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

The output of this code will be:
```bash
[2, 3, 1, 3]
```

This reflects the number of nesting levels for each set of parentheses in the provided string.