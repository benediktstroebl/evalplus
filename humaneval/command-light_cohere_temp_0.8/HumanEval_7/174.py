```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python script defines a function called `filter_by_substring` that filters an input list of strings based on whether the substring is found in that string. It uses the `find()` function to search for a substring within each string in the list.