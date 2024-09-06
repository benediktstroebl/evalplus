```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        level = 0
        nesting_level = 0
        for char in bracket_level:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
                if level == 0 and nesting_level > 0:
                    nesting_level -= 1
        result.append(nesting_level)
    return result
```

This script takes a string `s` that represents multiple groups for nested parentheses separated by spaces, and returns a list of the deepest level of nesting of parentheses for each group. 

The code iterates over each bracket level, maintaining a level variable that keeps track of the balance of open and closed parentheses at each level. It also maintains a `nesting_level` variable that keeps track of the maximum depth of nesting encountered in each group. Each time an open parenthesis is encountered, the `level` is incremented, and each time a closed parenthesis is encountered, the `level` is decremented. If a closed parenthesis is encountered when the level is zero, it means a complete nesting group has been closed, and the `nesting_level` is decremented.

The result is a list that contains the maximum depth of nesting for each bracket group in the provided string.

This solution has a time complexity of `O(n)` where n is the number of characters in the string, as it iterates over each character in the string only once. It has a space complexity of `O(n)` as it creates a new list to store the results.