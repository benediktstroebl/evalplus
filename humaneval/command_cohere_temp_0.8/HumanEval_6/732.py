```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        current_level = 0
        for char in chunk:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
            result.append(current_level)
    return result
```

The code splits the input string into spaces and then loops through each fragment, keeping track of the current parentheses level with a counter. When the counter goes up (exceeding a threshold), it adds to the result. When it goes down, it subtracts from the result.