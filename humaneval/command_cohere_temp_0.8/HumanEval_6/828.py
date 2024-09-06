```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ')) for _ in ' '*len(s)]]):
        result.append(len(opening))
    return result
```

The Python script provides a self-contained function `parse_nested_parens` takes a string as input and returns a list of deepest levels of nesting of parentheses in each group separated by spaces. For each opening parenthesis, it counts the closing parenthesis to calculate the current depth and uses `zip*` to iterate over all opening and closing parentheses. The result is a list containing the maximum depth of nesting for each group.