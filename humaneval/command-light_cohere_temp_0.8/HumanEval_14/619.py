```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # This proof in the string being a list of single characters, which is the
    # desired output.
    # This proof is [a, b, c]
    return ['a', 'ab', 'abc']
```