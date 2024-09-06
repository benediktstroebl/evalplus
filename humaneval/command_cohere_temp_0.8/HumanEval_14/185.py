```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate(string[::-1]))[::-1]
```
The function `all_prefixes()` uses the `accumulate()` function to create a list of all prefixes of the input string. The accumulated prefixes are reversed and then reversed again to be in the correct order (from shortest to longest).

The implementation uses a reversal (first reversing the input string and then reversing the accumulated prefixes) to avoid additional complexity and memory overhead that would be required by manual concatenation.