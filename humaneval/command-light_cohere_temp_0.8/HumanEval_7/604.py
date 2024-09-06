```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function filters an input list of strings to return only the ones that contain the given substring. The function utilizes the filter() function along with the contains() method to achieve this. This script is a most concise and self-contained manner.