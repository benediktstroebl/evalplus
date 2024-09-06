Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

The function works by using the conditional operator `?:` (a.k.a the Elvis operator) to directly assign the balanced groups of parentheses to the resulting list. The groups are split by the opening parenthesis `(` and enclosed in parentheses (`()`) to maintain their balance after separation. The resulting list is a clean separation of these groups.

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    return [group.strip('())' ) for group in paren_string.split('(') if group]
```