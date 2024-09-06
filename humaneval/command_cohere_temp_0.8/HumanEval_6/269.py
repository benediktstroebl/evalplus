```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nest in s.split():
        nest = list(nest)
        depth = 0
        while nest:
            if nest.pop() == '(': depth += 1
            else:
                depth -= 1
        result.append(depth)
    return result
```
The `parse_nested_parens` function takes a string `s` as input, where each nested group of parentheses is separated by spaces. It iterates through each of these groups, and maintains a `depth` counter that keeps track of the current nesting level. It does so by counting opening parentheses ('(') and subtracting the count of closing parentheses (')') encountered. The resulting deepest nesting level for each group is added to the `result` list, which is returned afterwards.

This solution assumes that the input string follows the given problem statement's expectations. Particularly, it assumes that each group of parentheses is separated by spaces, and that there are no redundant parentheses that might cause a syntax error.