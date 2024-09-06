```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:]))), [])))) for x in s.split()]
```

The provided Python script defines a function called `parse_nested_parens` that takes a string `s` as input. This string `s` contains multiple groups of nested parentheses separated by spaces. The function returns a list where each element represents the deepest level of nesting of parentheses in its corresponding group. To achieve this, we iterate over the string `s` splitting by spaces to get each separate group of parentheses. For each group, we convert it into a list of pairs, where each pair represents an opening and closing parenthesis. We then sum these lists of pairs by combining them into a list of tuples, and finally, we reverse the list and find the maximum depth by counting the number of pairs in half. This maximum depth represents the deepest level of nesting of parentheses in each group. The function returns a list that contains the result for each group.