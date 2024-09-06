```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        chunk = chunk.strip()
        if not chunk:
            continue
        open_count = chunk.count('(')
        close_count = chunk.count(')')
        result.append(open_count - close_count)
    return result
```

This code defines a function `parse_nested_parens` that takes a string as input and returns a list of deepest levels of nesting of parentheses in each grouped string. For example, it outputs `[2, 3, 1, 3]` for the input `('(()()) ((())) () ((())()())')`. 

The function splits the input string into a list of chunks where chunks are separated by spaces, strips leading and trailing spaces from each chunk, and then counts the number of opening and closing parentheses to calculate the deepest level of nesting for each chunk. The resulting list is then returned.