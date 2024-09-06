```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This script provides a self-contained function that filters an input list of strings, finding all substrings that are present in the input list.