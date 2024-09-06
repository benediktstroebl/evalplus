```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate(string[1:])) + [string]
```
This code uses the `accumulate` function from the `itertools` module to generate all prefixes of the input string. The function accumulates characters in the string to create prefixes one by one. It starts from the second character because the empty prefix is considered the first prefix and is already included in the input string. The list of accumulated prefixes is then added to the input string, ensuring that all prefixes are included in the result. The output is a list of prefixes ordered from shortest to longest.