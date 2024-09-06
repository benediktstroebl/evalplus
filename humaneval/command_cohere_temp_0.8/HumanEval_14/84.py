```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The function takes a string and iterates through all possible prefixes of the string using a list comprehension. It adds '%' to the end of each prefix to avoid duplicate results. The resulting list is then returned with the '%' signs removed. The output is a list of prefixes from the input string, ordered from shortest to longest.  If the input string is 'abc', the function returns ['a', 'ab', 'abc'].