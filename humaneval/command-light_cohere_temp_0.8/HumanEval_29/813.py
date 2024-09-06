Here is a self-contained Python script with a function that filters Markdown code blocks based on their prefixes:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The function takes two parameters: `List[str]` (an input list of strings) and `prefix: str` (the prefix to filter for). The function returns a new list that contains all the strings from the input list that start with the given prefix. This list will only contain strings that match the given prefix, and will be the only elements in the resulting list.