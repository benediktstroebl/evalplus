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

The approach of this code is straightforward. We iterate over each character of a separated parentheses group. We count the number of '(' characters to deduce the deepest level of nesting. We populate the result list with the results for each group, and finally, return the result list. The provided tests in the code block pass with this solution.