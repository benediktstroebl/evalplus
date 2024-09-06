```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for seperated_group in s.split():
        counter = 0
        for char in seperated_group:
            if char == '(':
                counter += 1
            else:
                counter -= 1
        result.append(counter)
    return result
```
The code uses a simple approach to parse the string and counts nesting levels varying from 0 to infinity. Each opening parenthesis increases the counter by 1, and each closing parenthesis decreases it by 1. The result array stores the maximum nesting level for each group of parentheses and is separated by spaces.