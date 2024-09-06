```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    return list(accumulate([string[::-1]]))[::-1]
```

The function `all_prefixes()` leverages the `accumulate()` function from the `itertools` module to generate all prefixes of the input string. Specifically, the list comprehension `[string[::-1]]` creates a list where each element is a substring of the reverse of the input string. For example, if the input string is 'abc', this list would be ['c', 'bc', 'abc']. The `accumulate()` function then applies a cumulative concatenation to the reversed list, so the result of `accumulate([string[::-1]])` is ['', 'c', 'bc', 'abc', 'abc']. The list is then reversed to obtain the correct order of prefixes from shortest to longest, and it's returned.

This approach avoids the unnecessary reversal of the entire list of prefixes, making it more efficient.