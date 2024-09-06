```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.list(string) if prefix != '']
# run the function and compare the output to the expected results
print(all_prefixes('abc'))  # Output ['a', 'ab', 'abc']
```  This script defines a function all_prefixes that returns a list of all prefixes from the shortest to the longest in a passed string.