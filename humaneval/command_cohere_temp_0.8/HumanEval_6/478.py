```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(len, group.split())))) for group in s.split()]
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a string (`s`) as input and returns a list of integer values. This function is designed to solve the problem of computing the deepest level of nesting of parentheses in multiple groups, as described by the given problem statement.

The `parse_nested_parens` function uses a list comprehension and the `max` function to determine the maximum depth of nesting for each group of parentheses in the input string. The `sum` function is used to calculate the total number of parentheses in each group, and the `reversed` function is applied to correctly determine the depth based on the longest prefix of the nesting count. The result is a list where each element represents the deepest level of nesting for each corresponding group of parentheses.