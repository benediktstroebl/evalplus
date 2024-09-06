```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group), [])))) for group in s.split()]
```

The provided Python script defines a function called `parse_nested_parens` which takes a string (`s`) as input. This string contains multiple groups of parentheses separated by spaces. The function returns a list where each element represents the maximum depth of nesting of parentheses within a particular group.

To achieve this, the function iterates over the string `s` splitting it into a list of parentheses groups. For each group, it converts it into an integer using `int(group)` which represents the number of opening parentheses `(`) in that group. Then, it uses a list comprehension to calculate the maximum depth of nesting by counting the number of closing parentheses `)` needed to balance each opening parenthesis, effectively calculating the number of nesting levels (`i // 2`) for each group. The results are reversed to ensure the maximum depth is correctly identified. Finally, the maximum depth of nesting for each group is returned as a list.