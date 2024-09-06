```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    return list(accumulate(string[::-1]))[::-1]
```

The function `all_prefixes()` uses the `accumulate()` function to generate all successive prefixes of the input string. This is achieved by reversing the string and accumulating characters from the end to the beginning, which ensures that the prefixes are generated in the correct order (from shortest to longest). The result is then reversed again to return the prefixes in their natural order. This approach eliminates the need for explicit loops, making the code more concise and readable.