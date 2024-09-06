```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_depth in map(count_bracket_depth, s.split()):
        result.append(bracket_depth)
    return result
    
def count_bracket_depth(s: str) -> int:
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0: 
            return count // -2
    return count
```

The `count_bracket_depth` function counts the number of open parentheses `'('` relative to the number of closing parentheses `')'`. The result is 0 for equality, positive for excess opening parentheses, and negative for excess closing parentheses. The excess is calculated by dividing the count by `-2` which flips the sign and doubles the magnitude.

The `parse_nested_parens` function splits the input string into individual parentheses groups using spaces as delimiters. For each of the groups, it invokes the `count_bracket_depth` function to measure the depth of the nesting and appends these values to the result list. The resulting list gives the deepest level of nesting for each of the groups of parentheses.