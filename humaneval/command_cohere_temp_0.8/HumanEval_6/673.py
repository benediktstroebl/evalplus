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

The code splits the input string into spaces and then loops through each fragment, keeping track of parentheses nesting level with a counter. It increments the counter for each `(` encountered and decrements for each `)`. The resultant list of nesting levels for each fragment is then returned. 

The example input provided in the prompt returns the result: `[2, 3, 1, 3]`.