```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It uses the string slicing to filter out any strings from the input list that start with the given prefix. The output is a list of strings from the input list that match the given prefix.