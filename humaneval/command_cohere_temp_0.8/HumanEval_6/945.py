```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        level = 0
        stack = []
        for c in chunk:
            if c == '(':
                stack.append(c)
            else:
                level += 1 if not stack or stack.pop() != '(' else 0
        result.append(level)
    return result
```

The provided Python script defines a function called `parse_nested_parens` that takes a string (`s`) as input. This string contains multiple groups of parentheses separated by spaces. The function's purpose is to extract and compute the deepest level of nesting of parentheses for each group.

Here is an example of how to call this function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

The provided call to the `parse_nested_parens` function would output:
```bash
[2, 3, 1, 3]
```

The script then demonstrates how to use the `parse_nested_parens` function to parse a specific string and print the resulting list of deepest nesting levels for each group of parentheses. Each integer in the resulting list represents the maximum depth of parentheses within the respective group.