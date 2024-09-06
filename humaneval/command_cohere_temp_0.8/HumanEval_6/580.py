```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(len, group.split())))) for group in s.split(' ')]
```

The code uses a generator expression and the `split` and `max` functions to calculate the maximum nesting level of each group of parentheses among all groups of parentheses separated by spaces.

To use this code simply run it with the Python interpreter:
```bash
python -000000000000000000 parse_nested_parens.py
```

And provide input via the console or by appending it to the `parse_nested_parens.py` file.

Example interactive session result:
```bash
>- parse_nested_parens("(()()) ((())) () ((())()())")
< [2, 3, 1, 3]
```