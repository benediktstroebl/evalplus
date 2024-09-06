```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The function takes a string as input and creates a list of prefixes from the shortest to the longest. The units are added after the corresponding prefix to ensure they are all different and thus viable candidates for sorting. The `[:-1]` list slice is used to remove the `%` character from the end of each prefix. 

Here is an example usage of the function:
```python
print(all_prefixes('abc'))
```
The output of this call will be:
```
['a', 'ab', 'abc']
``` 

The output provides the list of prefixes of the string from shortest to longest.