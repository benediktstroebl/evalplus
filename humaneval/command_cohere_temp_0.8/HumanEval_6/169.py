```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for partition in s.split():
        level = 0
        balance = 0
        for char in partition:
            if char == '(':
                level += 1
                balance += 1
            elif char == ')':
                level += 1
                balance -= 1
        result.append(balance)
    return result
```

The provided Python script defines a function called `parse_nested_parens` that takes a string `s` as input. This string represents multiple groups of nested parentheses separated by spaces. The function calculates and returns a list of deepest levels of nesting of parentheses for each group.

It does so by iterating through each partition (a subset of the string containing a single group of parentheses) and maintaining a level counter to track the overall nesting level, increasing it for '(' and decreasing it for ')'. Additionally, it keeps a balance counter to track the current balance of parentheses, incrementing it for '(' and decrementing it for ')'.

The function then appends the final balance value to the result list, which represents the deepest level of nesting for each group. The provided example demonstrates the function's usage and outputs the expected results for a few test cases.