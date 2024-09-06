```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    return list(accumulate([string[::-1], [character for character in string]])[0])
```

The function `all_prefixes()` uses the `accumulate()` function to generate all prefixes of the input string. Specifically, it joins the reverse of the string together with each character in the string to produce all prefixes from shortest to longest. It returns a list where each element is a prefix of the string, ordered from shortest to longest.