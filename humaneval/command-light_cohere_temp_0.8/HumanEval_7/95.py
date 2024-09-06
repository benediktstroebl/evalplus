```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This function uses the contains() method to check if each string in the input list contains the given substring. It returns a string as a list of strings that contain the substring. 

I have also added type hints using `from typing import List` and `substr` to provide better type definition for the function parameters and return value.