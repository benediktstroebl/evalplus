```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), (c for c in s.split(' ') if c)))))]
```

This code uses the zipper algorithm to compute the length of the longest common prefix in each line and then compute the maximum value in the resulting list of lengths.

The zipper algorithm is a way of traversing trees, arrays, and other structures while maintaining an efficient access to both previous and next elements. It allows to efficiently extract a prefix of members in a list. 

The function `parse_nested_parens` takes a string as input and returns a list of the maximum depth of nesting for each group of parentheses. The function initially splits the string into a list of strings separated by spaces. Then for each string of parentheses, it zips them (makes pairs out of them) and reverses them to get the longest common prefix efficiently using the zipper algorithm. After, it simply finds the maximum depth of nesting by counting the number of pairs (which is half of the parentheses count) in the reversed zipper list.