```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])),
        (subscript := s.split(' ')))))) for _ in range(len(subscript))]
```

The solution works by:
1. Splitting the input string into a list of substrings, each containing a group of parentheses.
2. For each substring, mapping each pair of corresponding parentheses to a list `[x, x[1:]]`, where `x` is the index of the opening parenthesis.
3. Summing up the lists to get the indices of the opening parentheses.
4. Reversing the list of indices and dividing it by 2 to get the deepest level of nesting for each substring.
5. Returning a list containing the deepest level of nesting for each group of parentheses.