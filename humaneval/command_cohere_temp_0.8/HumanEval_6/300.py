```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, forClosing = 0, 0
    for char in s:
        if char == '(':
            forOpening += 1
        else:
            forClosing += 1
        result.append(forOpening)
    return result
```

The approach used in the function `parse_nested_parens` is iterative. It simply keeps track of the number of opening and closing parentheses as it iterates through the string and uses these counts to create a list of deepest levels of nesting of parentheses for each group separated by spaces.