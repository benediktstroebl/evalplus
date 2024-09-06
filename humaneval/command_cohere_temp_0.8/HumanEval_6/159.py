```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        open_parentheses = token.count('(')
        close_parentheses = token.count(')')
        result.append(open_parentheses - close_parentheses)
    return result
```

The `parse_nested_parens` function takes a string as input and splits it by spaces to iterate over each token (or group of parentheses) and determines the nesting level by counting the number of open parentheses and subtracting the number of close parentheses. The result is a list where each item represents the deepest nesting level of each group of parentheses.