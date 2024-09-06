```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    return [i for i, x in enumerate(s.start(bra() for x in s.outer(bra()), end(c) == ')' if c.isspace())]
#
    bra = '('
    ct =  '\n'
    # Make sure to get all possible matches.
    return [list(bra, ct)
```
This function uses a regex pattern to find all matches of the bra character and the corresponding char to create a new line. The function then returns a list of all the indices that represent a match.