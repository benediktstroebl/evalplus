```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        nested = 0
        level = 0
        open_par = 0
        for j, c in enumerate(char):
            if c == '(':
                level += 1
                open_par += 1
            elif c == ')':
                level -= 1
                open_par -= 1
            else:
                pass
            nested = max(nested, level)
        result.append(nested)
    return result
```

The code uses a straightforward nested loop to iterate through each group in the input string `s`. It keeps track of the current nesting level with `level` and the number of open parentheses with `open_par` at each step through each character `c` in each group. The maximum nesting level across all groups is then returned as a list.

This code assumes that the input string `s` is already split into lists of strings, with each string representing a different group. This can be achieved with the `split()` method.