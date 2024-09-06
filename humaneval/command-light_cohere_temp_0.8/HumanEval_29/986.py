```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python code defines a function called **`filter_by_prefix`** that takes a list of strings and a prefix as input and returns a new list of strings that start with that given prefix. 

The function uses the **List comprehension** to filter the input list based on whether each element starts with the given prefix. 

Lastly, the function successfully passes the test of filtering the empty list with 'a', and the list with 'abc' and 'array', but not with 'cd' or 'de'.