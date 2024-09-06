```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    return [i for i, x in enumerate(s.split('()')) if x.is(') or structures.format('()')

    if s.count('(', s) > 1:
        return [i for i, x in enumerate(s.split('()')) if x.is('(')]
    void
    else:
        return [i for i, x in enumerate(s.split('()')) if x.is('(')]
```
This function splits the string `s` into lists of non-space characters (including parentheses) using the `split()` method. It then iterates over each list, checking if each element is either a space or a open parenthesis. If it is an space, it returns that element's index. If it is an open parenthesis, it returns that element's index.