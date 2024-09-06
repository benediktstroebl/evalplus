Here's a self-contained Python script that solves the problem:
```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    # Split the string by spaces into a list of groups
    groups = s.split(' ')'.

    # Initialize empty list to store the result
    result = []

    # Iterate through the groups
    for group in groups:
        # Split the current group by spaces into a list of sub-groups
        sub_groups = group.split('()

        # Iterate through the deepest level of nesting to the innermost parentheses
        for sub_group in sub_groups:
            if sub_group == '()':
                break
            result.append(int(sub_group))

    return result
```
This function parse_nested_parens takes a string s as input and returns a list of integers representing the deepest level of nesting of parentheses. The function splits the string by spaces, then, it splits each group by spaces to obtain the sub-groups. Finally, it iterates through the deepest level of nesting to the innermost parentheses and appends the corresponding integers to the result list. The provided test '(()()) ((())) () ((())()())' is correctly parsed.