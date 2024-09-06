```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_group in s.split():
        count = 0
        imbalance = 0
        for char in bracket_group:
            if char == '(':
                count += 1
                imbalance += 1
            else:
                count -= 1
                if count < 0:
                    imbalance += 1
        result.append(imbalance)
    return result
```

The provided Python script defines a function called `parse_nested_parens` that takes a string input `s`, which represents multiple groups for nested parentheses separated by spaces.

This function calculates and returns a list where each element represents the deepest level of nesting of parentheses in each group. It achieves this by iterating through each bracket group in the input and maintaining a count of open parentheses `(` and a separate count of closed parentheses `)`. The `imbalance` variable keeps track of the difference between these two counts, which indicates the maximum depth of nesting within a group. Finally, the script returns a list containing the imbalance counts for each group.