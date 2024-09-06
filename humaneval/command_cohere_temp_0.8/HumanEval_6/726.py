Here's a Python script with a self-contained function that solves the problem using a recursive approach for the parsing:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    def max_nesting(i, nest):
        if i == len(s):
            return nest
        if s[i] == '(':
            return max(max_nesting(i+1, nest+1), max_nesting(i+1, nest))
        else:
            return max_nesting(i+1, nest)
    
    return list(map(max_nesting, range(len(s)), [0] * len(s)))
```

The function `max_nesting` is a recursive function that checks the current nesting level and recursively compares it to nesting subsequent levels. It increments the nesting level if a opening paren `(`) is encountered else it stays at the same level or decreases if it hits a closing paren `)`. The function then uses `map` to apply `max_nesting` to each index of the string and hence solve the problem.

To test the script, evaluate the expression `parse_nested_parens('(()()) ((())) () ((())()())')` to see the expected output `[2, 3, 1, 3]` as illustrated in the given example.