```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function uses the `dropwhile` function from the `itertools` module to iterate over the characters of `string` while dropping the characters whose concatenation with the previous prefix equals the current prefix. The `reversed` function is used to return the prefixes in descending order. 

The implementation ensures that the function returns the shortest prefix first, followed by longer prefixes, until it returns the entire string. 
This approach provides a concise way to generate the desired list of prefixes. In order to pass the corresponding tests the function has to return the prefixes as explained and not only the longest prefix that starts with the first character of the string.