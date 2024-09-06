```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        open_bracs = chunk.count('(')
        closed_bracs = chunk.count(')')
        result.append(open_bracs - closed_bracs)
    return result
```

The code splits the input string into chunks using spaces as separators, then counts the number of open and closed parentheses for each chunk separately and calculates the difference between these counts, which corresponds to the deepest level of nesting of parentheses in that particular chunk. The results are then collected into a list and returned. 

To ensure the function is self-contained and does not rely on any external dependencies like a parser library, it utilizes string splitting and basic string counting methods, making it fit for the provided problem.