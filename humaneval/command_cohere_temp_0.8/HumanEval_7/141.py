```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code snippet takes advantage of list comprehension to filter strings present in the 'strings' list that contain the specified 'substring'. It is also annotated with the `typing` module to make it more readable and provide hints to the types of the variables.