Here's the self-contained Python script that solves the problem of finding all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in string if i != ""].split("")
```
This script defines a function that returns a list of all prefixes from the shortest to the longest, by using the split method and a list comprehension.