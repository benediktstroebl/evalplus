```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nested_parens in s.split():
        current_level = 0
        for char in nested_parens:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
            result.append(current_level)
    return result
```

The logic behind this approach is straightforward. We iterate through each group of parentheses, tracking the current level of nesting with `current_level` variable. When we encounter a `(`, we increase the nesting level, and when we encounter a `)`, we decrease the level. Finally, we store the achieved level for each group in the result list.

To test this script, you can run the following code using an appropriate test case:
```python
test_cases = ['(()()) ((())) () ((())()())', '(((((()())))))', '()', '((()))', '(((((((()())))))))']

for case in test_cases:
    print(f'\nParsing the string {case}:\n{parse_nested_parens(case)}')
```

This should output the results as described in the original problem statement.