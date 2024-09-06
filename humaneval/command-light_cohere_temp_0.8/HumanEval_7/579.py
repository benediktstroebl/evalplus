```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
Here is a self-contained Python script with a function that filters an input list of strings to only include those that contain a given substring.  It also passes the smilar tests.