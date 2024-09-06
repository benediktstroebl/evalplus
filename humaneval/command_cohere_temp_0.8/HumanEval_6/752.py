```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nesting = 0
        for char in chunk:
            if char == '(':
                nesting += 1
            elif char == ')':
                nesting -= 1
            count = max(count, nesting)
        result.append(count)
    return result
```

The `parse_nested_parens` function takes a string as input and splits it into chunks using spaces as separators. It then iterates over each chunk, maintaining a count of nesting levels and a maximum count of open parentheses encountered. The maximum open parentheses count is used as the nesting level for that chunk. The results are returned as a list of integer values, where each value represents the deepest nesting level of parentheses in each corresponding chunk.

This solution passes the provided test case and will accurately parse different scenarios of nested parentheses. 

**NOTE:** The solution assumes that all input parentheses are well-formed and properly balanced. It does not handle ambiguous or incorrectly structured input scenarios.