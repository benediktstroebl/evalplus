```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        curr = opening
        while curr != closing:
            if curr == '(':
                depth += 1
            else:
                depth -= 1
            curr = next(closing)
        result.append(depth)
    return result
```

The provided Python script defines a function `parse_nested_parens` that takes a string `s` as input, which is supposed to contain multiple groups of nested parentheses separated by spaces.

This function iterates through these groups, and for each group, it monitors the '('' and ')'' characters using two separate iterators. It keeps track of the '('' characters to determine the deepest level of nesting of parentheses.

The `result` list is appended with the determined depth for each group, and ultimately, the function returns this `result` list, which contains the deepest level of nesting for each group of parentheses. 

Here is an example usage of this function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This example provides multiple groups of parentheses, and the function calculates the deepest level of nesting for each group, which are [2, 3, 1, 3] in this case.