```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
The function uses the `contains` method to iterate over the input list and return only the elements that contain the given substring. The code is self-contained and passes the test cases.