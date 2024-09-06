```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(range(len(x)) + [0]), s.split())))) for _ in range(len(s.split()))]
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a string (`s`) as input and returns a list of integers. This function is designed to solve the problem of computing the deepest level of nesting of parentheses in each of the groups separated by spaces in the input string.

The function uses a combination of list and map operations to aggregate the parentheses depths for each group. It splits the input string into a list of substrings based on spaces, and then uses a map function to convert each substring into a list of indices representing the parentheses positions. The deepest level of nesting is determined by finding the maximum depth (calculated as `i // 2`) for each sublist, obtained from the `sum` function. Finally, the maximum depths for each group are returned as a list.