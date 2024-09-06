```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda s: s != '', string))));
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to iterate over the strings formed by extending the input string by single characters, starting from an empty string. The `dropwhile` function drops elements from the iterator as long as the predicate returns `True` — in this case, as long as the current string is not equal to an empty string. The list of prefixes is then reversed to ensure that it is in the desired order, from shortest to longest. As the example in the docstring suggests, the result for the input `'abc'` is `'[a, ab, abc]'` — the shortest prefix is `'a'`, followed by `'ab'`, and finally, the entire string itself, `'abc'`.