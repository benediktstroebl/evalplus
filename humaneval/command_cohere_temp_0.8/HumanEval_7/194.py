```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code takes advantage of list comprehension to filter strings that contain the given substring from the given list of strings.

```python
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
``` 

The example tests cases in the original markdown code snippet to show the function's correct operation.