```python
from typing import List
from itertools import accumulate

def all_prefixes(string: str) -> List[str]:
    return list(accumulate(string[::-1]))[::-1]
```

The function `all_prefixes()` leverages the `accumulate()` function from the `itertools` module to generate all prefixes of the input string. Accumulate accepts a function and an iterable (in this case, a string reversed using slicing) and returns the progressive accumulation of applying the given function to each element of the iterable. In this context, the function logically considered is the concatenation operation, encapsulated in the `__add__` method.

The progressive concatenation is reversed back to obtain the correct order of prefixes, and the resulting list of prefixes is then reversed again to ensure the correct order from shortest to longest. 

This approach eliminates the need for explicit loops, making the code more efficient and concise.