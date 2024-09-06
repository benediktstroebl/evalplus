```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', '))').enumerate()]):
        nest_level = opening
        while closing != len(s) and s[closing] == '(':
            nest_level += 1
            closing += 1
        result.append(nest_level)
    return result
```

The provided Python script defines a function `parse_nested_parens` which accepts a string `s` that represents multiple groups for nested parentheses separated by spaces. This function processes each group independently by iterating through the opening and closing parentheses, incrementing a counter for each opening parenthesis encountered, and resetting it whenever a closing parenthesis is met. The final count, representing the deepest level of nesting for each group, is collected in a list and returned.

The example usage and test cases are omitted as they are not necessary for a self-contained script. You can add them later if needed.