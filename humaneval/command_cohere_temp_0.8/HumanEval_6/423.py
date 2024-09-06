```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nested = 0
        i = 0
        while i < len(chunk):
            if chunk[i] == '(':
                count += 1
                nested += 1
            elif chunk[i] == ')':
                count -= 1
            i += 1
        result.append(nested)
    return result
```
The `parse_nested_parens` function takes a string as input and splits it into chunks using spaces as separators. It then iterates over each chunk and maintains a count of open parentheses '(' and subtracts a count of closed parentheses ')' to calculate the maximum nested level of parentheses in each chunk. The result is a list of these maximum nesting levels for each chunk, which represents the output of the function.