```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        level = 0
        unbalanced = 0
        for char in bracket_level:
            if char == '(':
                unbalanced += 1
            elif char == ')':
                unbalanced -= 1
            level = max(level, unbalanced)
        result.append(level)
    return result
```

The provided Python script defines a function called `parse_nested_parens` that takes a string (`s`) as input. This string contains multiple groups of nested parentheses separated by spaces. The function calculates the deepest level of nesting of parentheses for each group and returns a list of these values. It does this by iterating through each group of parentheses and maintaining a `level` variable that keeps track of the maximum depth of parentheses encountered. It also keeps track of the unbalanced parentheses with the `unbalanced` variable. At the end of each group, it updates the `level` with the maximum of its current value and the `unbalanced` variable. The result is a list that contains the deepest level of nesting for each group of parentheses in the input string.