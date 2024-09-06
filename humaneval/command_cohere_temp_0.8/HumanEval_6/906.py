```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for partition in s.split():
        level = 0
        curr = 0
        for c in partition:
            if c == '(':
                curr += 1
            else:
                curr -= 1
            level = max(level, curr)
        result.append(level)
    return result
```

The `parse_nested_parens` function takes a string as input and iterates through each partition of the string divided by spaces. It keeps track of the current nesting level `level` and the current parentheses count `curr` for each partition. It increments `curr` for each opening parenthesis `(` and decrements it for each closing parenthesis `)`. The maximum value between the current partition's `curr` and the previous `level` is used as the new `level`. The function returns a list of these maximum nesting levels for each partition.

Here is an example usage of the function:
```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

The output of this example will be:
```bash
[2, 3, 1, 3]
```

This example string has multiple groups of nested parentheses separated by spaces, and the function will return a list of the deepest level of nesting of parentheses for each group.  The result for the example above is [2, 3, 1, 3], because the first two groups have depths of 2 and 3, the third group has a depth of 1, and the fourth group has a depth of 3.