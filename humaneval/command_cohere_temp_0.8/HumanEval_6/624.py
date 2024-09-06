```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair in s.split():
        levels = 0
        i = 0
        while i < len(bracket_pair):
            if bracket_pair[i] == '(':
                i += 1
                levels += 1
            else:
                i += -1
                levels -= 1
        result.append(levels)
    return result
```
The Python script uses a simple approach to solve the problem. It iterates through each bracket pair separated by spaces, and counts the number of '(' and ')' to calculate the number of nesting levels. The function returns a list with the result for each bracket pair. 

This solution has a time complexity of O(n), where n is the number of bracket pairs in the input string.