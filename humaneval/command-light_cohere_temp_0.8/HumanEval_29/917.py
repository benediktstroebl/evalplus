```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function uses a generator expression with a filtering condition to return only the strings that start with the specified prefix. 

Here's a sample output:
```
['abc', 'array']
``` 
This is consistent with the problem's documentation. 

This function demonstrates a clear and concise way to filter data based on a prefix, which is a common task in many programming scenarios.