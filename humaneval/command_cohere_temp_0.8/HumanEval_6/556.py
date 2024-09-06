```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group.split())))) for group in s.split(' ')]
```

The logic of the function is as follows:
1. Split the input string `s` into a list of strings, where each string represents a group of parentheses.
2. For each group, convert it to a list of integers representing the depths of parentheses, by interpreting each open parenthesis `(` as `1` and each closed parenthesis `)` as `-1`.
3. Sum up the integers in each list to get a list of sums, where each sum represents the total depth of all parentheses in a given group.
4. Maximum nesting depth in each sum is calculated by finding the maximum depth achieved when iterating through the sum in reverse and incrementing/decrementing `i` by `1` for each open/closed parenthesis.
5. The maximum depth of all groups is returned as a list.

This approach ensures that the maximum depth of nesting for each group of parentheses in the given string is accurately calculated.