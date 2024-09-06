Here's the function that filters out words in a list that starts with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [word for word in strings if word.startswith(prefix)]
```

This function takes a list of strings and a prefix as arguments. It uses the filtering to create a new list that contains only the words from the original list that start with the given prefix. The function uses the simple Python and can easily be adapted to other problems involving string filtering with prefixes.