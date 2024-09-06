```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in map(len, s.split()):
        result.append(bracket_level)
    return result
```

The specified Python script solves the problem of parsing nested parentheses in a given string. It uses a simple approach to split the input string into individual bracket sequences using spaces as separators, and then calculates the deepest level of nesting for each sequence by counting the number of opening and closing parentheses. The result is a list that contains the maximum nesting level for each bracket sequence.