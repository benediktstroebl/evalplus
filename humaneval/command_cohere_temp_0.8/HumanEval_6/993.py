```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_seq in s.split():
        current_level = 0
        nested = 0
        stack = [current_level]
        for char in bracket_seq:
            if char == '(':
                current_level += 1
            else:
                current_level -= 1
                nested = max(nested, current_level)
            stack.append(current_level)
        result.append(nested)
    return result
```

The code processes each sequence of brackets separately and calculates the deepest level of nesting for each of them. It does so by keeping track of the current level of nesting with `current_level`, and tracking the maximum level of nesting achieved `nested` while looping through each character in the sequence. The `stack` is used to track the historical maximum levels of nesting, so that the maximum can be correctly updated when a new maximum is encountered.