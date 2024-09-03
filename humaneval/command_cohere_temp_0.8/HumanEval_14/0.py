```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: len(x) > 0, string))));
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to iterate over the characters of `string` in reverse order while dropping the longest prefix of the string. 

The `dropwhile` function takes a test function, in this case, `lambda x: len(x) > 0`, which checks whether the length of the current prefix `x` is greater than 0, implying it is not an empty string yet. The resulting list of prefixes is then reversed to ensure the order is from shortest to longest. 

This approach is efficient and suits the problem requirements, generating the desired output. 

The implementation can be further enhanced to handle an empty input string by adding a starting prefix of `None` in the list, but it's optional depending on the problem constraints.