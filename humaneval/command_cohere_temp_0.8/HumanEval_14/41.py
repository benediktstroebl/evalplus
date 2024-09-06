```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    return list(accumulate(string[::-1]))[::-1]
```

The function `all_prefixes()` uses the `accumulate()` function to create a list of all prefixes of the input `string` in reverse order, and then reverses that list to get the prefixes in the desired order. This method proves efficient and elegant in its use of built-in Python functions to solve the problem.