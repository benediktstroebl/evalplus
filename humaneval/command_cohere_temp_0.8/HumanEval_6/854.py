```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        chunk = chunk.replace('(', '')
        chunk = chunk.replace(')', '')
        result.append(len(chunk))
    return result
```

The `parse_nested_parens` function takes a string as input and splits it into chunks based on the spaces, then removes all opening and closing parentheses from each chunk. It then calculates the length of each chunk to represent the deepest level of nesting of parentheses, and returns a list of these values. 

To ensure performance improvements for large inputs, the script avoids nested loops by only employing iterative procedures, which prove efficient for parsing and manipulating strings.

This solution achieves a linear time complexity of O(n), where n represents the input string length, as it operates straightforwardly on the input characters without any nested loops. Thus, efficiency is preserved regardless of input length.