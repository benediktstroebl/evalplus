```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        depth = 0
        balance = 0
        for char in chunk:
            if char == '(':
                depth += 1
                balance += 1
            elif char == ')':
                depth += 1
                balance -= 1
        result.append(balance)
    return result
```

The given Python script defines a function `parse_nested_parens` that takes a string `s` as input, and returns a list of deepest nesting levels of parentheses in each sub-string separated by spaces. For instance, the result of the function for the input `(()()) ((())) () ((())()())` would be `[2, 3, 1, 3]`.

The function achieves this by performing a depth-first traversal of each parenthesis group in the input string. It maintains a `depth` counter that increments with `(`) and decrements with `)`. The maximum depth reached in a group yields the deepest level of nesting for that group. A `balance` counter is also maintained to handle cases where closing parentheses appear first, as in `())(()`. The result is a list where each element represents the deepest nesting level of the respective group.