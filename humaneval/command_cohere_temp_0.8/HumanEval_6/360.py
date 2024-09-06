```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        level = 0
        unbalanced = 0
        nesting_level = 0
        for char in bracket_level:
            if char == '(':
                nesting_level += 1
                unbalanced += 1
            elif char == ')':
                nesting_level += -1
                unbalanced -= 1
            if unbalanced > 0:
                continue
            result.append(nesting_level)
            unbalanced = 0
        if unbalanced > 0:
            result.append(nesting_level)
            unbalanced -= 1
    return result
```

The approach for this Python script involves:
1. Splitting the input string by spaces into different strings, each representing a different group of parentheses.
2. For each group, iterates through its characters, keeping track of the nesting level and unbalanced parentheses.
3. If there are unbalanced open parentheses, the loop skips to the next group, ensuring that the nesting level of the entire group is recorded at the end.
4. The resulting list contains the maximum nesting level for each group.