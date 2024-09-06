```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group), [])))) for group in s.split(' ')]
```

The provided Python script defines a function called `parse_nested_parens` which takes in a string `s` as input. This string `s` contains multiple groups of parentheses separated by spaces. The function returns a list where each element represents the maximum depth of nesting of parentheses in the corresponding group.

To achieve this, the function uses a combination of integer conversion, summing, and maximum depth calculation within each group. It iterates over the groups of parentheses, splitting the input string at spaces. For each group, it converts them into integers using `map(int, group)`, which represents the number of opening parentheses `(`) encountered. The sum of these integers is then calculated using `sum(map(int, group), [])`, which gives the total count of opening parentheses. By calculating the maximum depth of nesting using `max(i // 2 for i in reversed(total_open, []))`, it determines the most nested group of parentheses.

The output of the function is a list where each element represents the maximum depth of nesting of parentheses in the corresponding group.