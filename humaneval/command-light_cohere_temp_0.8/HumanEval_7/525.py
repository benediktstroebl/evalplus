```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This Python script defines a function `filter_by_substring` that filters an input list of strings to include only those that contain a given substring. The function utilizes the `contains` to iterate over the list of strings and checks if each element contains the specified substring using the `contains` method.