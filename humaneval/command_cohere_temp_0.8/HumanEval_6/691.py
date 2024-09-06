```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(len, group.split())))) for group in s.split()]
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a string (`s`) as input and returns a list of integers. This function is designed to solve the problem of computing the deepest level of nesting of parentheses in each of the groups of a given input string that is separated by spaces.

Here's how it works:
1. The function uses a list comprehension and the `sum` function to calculate the total length of each group (a string of parentheses) in the input string.
2. The `map` function is used to convert each group into an integer representing the length of the group.
3. The sum operation in the list comprehension accumulates these lengths, and the `reversed` function is applied to reverse the list of lengths to ensure that the maximum depth is correctly calculated even if the group is not properly nested.
4. The `max` function is used to compute the maximum depth of nesting for each group, which is the number of parentheses divided by 2 (since each parentheses level is counted as 2).
5. Finally, the resulting list of maximum depths for each group is returned.