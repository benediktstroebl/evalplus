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

The given Python script defines a function called `parse_nested_parens` that takes a string `s` as input. This string is expected to contain multiple groups of nested parentheses separated by spaces. The function calculates the deepest level of nesting of parentheses for each group and returns the result as a list of integer values.

The inner loop iterates through each character of the current bracket level (`bracket_level`), the `unbalanced` counter keeps track of the imbalance of open and close parentheses at the current moment. Whenever an open parenthesis `(` is encountered, `unbalanced` is increased, and when a close parenthesis `)` is encountered, `unbalanced` is decreased. The maximum value of `unbalanced` over the entire group corresponds to the deepest level of nesting.

The given example test case `"(()()) ((())) () ((())()())"` returns `[2, 3, 1, 3]` as expected.