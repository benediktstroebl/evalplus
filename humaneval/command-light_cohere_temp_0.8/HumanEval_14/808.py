Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of a given input string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.split() if string.islr: len(string)]
```

This function splits the input string into a list of prefixes and then filters only the valid prefixes (those that are not empty). 

You can uncomment the function call and run it in your Python environment to test the function.