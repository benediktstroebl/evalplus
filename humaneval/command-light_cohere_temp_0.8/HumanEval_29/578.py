```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as parameters. It returns a the filtering the input strings by using the `startswith` function, which checks whether each string starts with the given prefix. 

The `List` function is used to iterate over the input strings and the `filter` function is used to filter the strings that start with the given prefix.