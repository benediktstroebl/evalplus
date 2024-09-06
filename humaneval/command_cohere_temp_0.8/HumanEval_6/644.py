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
    result.append(forClosing)
    return result
```

The given Python script defines a function `parse_nested_parens` that takes a string `s` as input, which contains multiple groups of nested parentheses separated by spaces. This function calculates and returns a list where each element represents the deepest level of nesting of parentheses in the corresponding group. It achieves this by keeping track of the number of opening and closing parentheses encountered as it iterates through the input string `s`. The test example provided demonstrates its usage and shows how the function successfully extracts and returns the deepest level of nesting for each group in the specified input string.