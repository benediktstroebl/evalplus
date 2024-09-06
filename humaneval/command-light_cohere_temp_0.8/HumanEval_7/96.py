```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
The function above effectively filters the input list of strings, returning a new list that contains only the elements that contain the specified substring. 

Note: this function is self-contained, and it does not require any additional variables or external functions to work.