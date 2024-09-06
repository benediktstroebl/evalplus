```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # if x == y: return [x]
    # for prefix in string.forall(lambda x: x != y for y in string)
    #   return [x] + all_prefixes(y)
    # return [x] + [all_prefixes(y) for y in string]
    # return [x] + [p for p in all_prefixes(y) if x != y]
    # return [x] + set([p for p in all_prefixes(y) if x != y])
    # return [x] + frozenset([p for p in all_prefixes(y) if x != y])
    # return [x] + list(all_prefixes(y) for y in string)
    # return [x] + [tuple(p) for p in all_prefixes(y)]
    # return [x] + [f(p) for p in all_prefixes(y)]
    # return [''.join(x) for x in string] if len(string) == 0
```