```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python function uses the `find()` method to check if each string in the input list contains the given substring. The function returns a list of strings that do contain the substring. 

Note that the function assumes that the input list of strings is non-empty and that the substring to search for is provided as the second argument.