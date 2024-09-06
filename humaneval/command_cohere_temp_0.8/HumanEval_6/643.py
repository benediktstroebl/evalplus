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

The code uses a simple approach to split the string into chunks by spaces, and then counts the number of open and closed brackets in each chunk, subtracting the two to get the deepest level of nesting of parentheses in that particular chunk. The results are then collected in a list and returned. 

To ensure the function is self-contained and does not rely on external modules, no additional imports are needed. The function handles the nested parentheses problem directly, making the code more concise and efficient, thus simplifying the overall solution.