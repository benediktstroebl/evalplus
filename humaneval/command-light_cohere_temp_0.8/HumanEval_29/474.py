Here is a self-contained Python script that implements the filter_by_prefix function, which is used to filter an input list of strings based on a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script provides a function that takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the specified prefix. 

Feel free to ask me anything about any other programming concepts or code related questions!