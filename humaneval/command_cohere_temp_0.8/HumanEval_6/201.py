```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(len, group.split())))) for group in s.split(' ')]
```

The logic of the solution is to treat each group from the input string s as a list of strings where each string is a subexpression enclosed in parentheses. Then, we calculate the length of each subexpression list and sum them up using the `sum` function. Finally, we retrieve the maximum depth of nesting for each group by calculating the maximum length divided by 2 (since each nesting level is represented by two additional characters '(' and ')' in the string). The maximum depth of nesting for each group is returned as a list.

This code assumes that the input string `s` is already correctly formatted with nested groups of parentheses separated by spaces as described in the problem statement. If the input format is not as expected, the code may not work as expected.