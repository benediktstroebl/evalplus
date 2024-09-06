```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        result.append(len(bracket_level) - 1)
    return result
```

The specified Python script solves the problem of parsing nested parentheses and returns the deepest level of nesting for each group in the input string separated by spaces.

The function `parse_nested_parens` takes a string `s` as input, which contains multiple groups of nested parentheses separated by spaces. It uses the split method to separate each group of parentheses and calculates the deepest level of nesting by subtracting 1 from the number of characters in each split string (since the last character is considered as the closing parenthesis). The resulting deepest levels of nesting for each group are stored in a list and returned.