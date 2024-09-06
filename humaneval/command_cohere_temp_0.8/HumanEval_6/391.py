```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for seperated_group in s.split():
        current_level = 0
        nested = 0
        for char in seperated_group:
            if char == '(':
                current_level += 1
                nested = max(nested, current_level)
            elif char == ')':
                current_level -= 1
        result.append(nested)
    return result
```

The specified Python script defines a single function `parse_nested_parens(s: str) -> List[int]`, which takes a string `s` as input. This string `s` is supposed to contain multiple groups of nested parentheses separated by spaces. The function calculates and returns a list of the deepest level of nesting of parentheses for each group.

The function iterates over each separated group and maintains a `current_level` counter that keeps track of the current nested level of parentheses '(' counted when encountering an opening parenthesis '('. At the same time, it maintains a `nested` counter that keeps track of the maximum nested level encountered so far.

When encountering a closing parenthesis ')', the `current_level` is decremented, and if `current_level` exceeds the `nested` counter, it updates the `nested` counter to the current `current_level`.

Finally, the function returns a list that contains the `nested` counter for each separated group, which represents the maximum depth of nesting of parentheses found within that group.

The specified script passes the provided tests as evidenced by the sample test case:
```
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

The expected result for the given example is `[2, 3, 1, 3]`, which is correctly produced by the script.