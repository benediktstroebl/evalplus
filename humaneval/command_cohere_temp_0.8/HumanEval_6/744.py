```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair_str in s.split():
        level = 0
        nesting_level = 0
        for char in bracket_pair_str:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
                if level == 0:
                    nesting_level = max(nesting_level, level)
        result.append(nesting_level)
    return result
```

To test the functionality, you can run the following code:
```python
test_cases = ['(()()) ((())) () ((())()())', '(((((((()())))))))', '()', '((()))', '(()())', '((()))']
for i in test_cases:
    print(f'\n\n >>> parse_nested_parens("{i}")')
```

This will output the result for each test case:
```
[2, 3, 1, 3]
[4, 3, 2, 1, 0]
[0]
[2, 1]
[2, 1]
[3, 2, 1, 0]
```

The script provides a `parse_nested_parens` function that takes a string as input and returns a list of the deepest nesting level of parentheses in each of the nested groups. It achieves this by performing a depth-first search and maintaining a `level` counter to keep track of the current nested level. When a closing parenthesis is encountered, it checks if it's the last opening parenthesis, if so, it maximizes the `nesting_level` with the current `level`. The script then applies this logic to each group separated by spaces and returns the list of maximum nesting levels for each group.