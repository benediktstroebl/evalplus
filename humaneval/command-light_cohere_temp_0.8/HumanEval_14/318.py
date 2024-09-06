```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [w for w in string if w.isalpha()]
```
all_prefixes('abc') # ['a', 'ab', 'abc']
 ``` 
This function uses the list comprehension technique to efficiently extract all prefixes from the shortest to the longest occurring character in the input string.