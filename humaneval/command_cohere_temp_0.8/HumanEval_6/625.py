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

This Python script includes a function (`parse_nested_parens`) that takes a string as input and returns a list of deepest levels of nesting of parentheses in each nested group separated by spaces. The provided example and test cases show how to call the function and check the result.