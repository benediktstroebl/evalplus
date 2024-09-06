```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        open_brace, close_brace = 0, 0
        for char in chunk:
            if char == '(':
                open_brace += 1
            elif char == ')':
                close_brace += 1
        result.append(open_brace/close_brace if open_brace else 0)
    return result
```

The code splits the input string into space-separated chunks, and then loops through each chunk to count the number of `(` and `)` characters. The deepest level of nesting is calculated by counting the number of open parentheses at the highest level and dividing it by the number of corresponding closing parentheses. The result list stores these values. The algorithm is designed to handle scenarios with different grouping formats and even empty chunks, resulting in an accurate depth measurement for each.