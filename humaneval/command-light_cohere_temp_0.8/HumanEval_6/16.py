```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [i for i, x in enumerate(s.split('()') if x.count('()') > 1]
```
This function splits the string `s` into substrings `t` based on whitespace characters and checks whether the length of each substr string is greater than 1. If it is, the corresponding index `i` in the returned list will be set to the deepest level of nesting of parentheses found in the substring `x`.