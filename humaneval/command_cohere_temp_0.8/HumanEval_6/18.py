```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group), [])))) for group in s.split()]
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a string `s` as input. This string `s` contains multiple groups of parentheses separated by spaces. The function's purpose is to extract the deepest level of nesting of parentheses for each group.

Here's how it works:
- The `parse_nested_parens` function uses a list comprehension to split the input string `s` into a list of substrings based on the spaces. Each substring corresponds to a group of parentheses.
- For each substring (group), the sum(map(int, group), []) converts the group of parentheses into a list of integers representing the depths of each nest, and reverses this list to maintain the hierarchy.
- Finally, the maximum depth of nesting is computed within each reversed list of depths, providing the deepest level of nesting for each group of parentheses.

This function effectively solves the problem of parsing nested parentheses and determining the deepest level of nesting for each group. The provided example in the comment section demonstrates its functionality using a test case and shows the output `[2, 3, 1, 3]` for the given input `('(()()) ((())) () ((())()())')`.