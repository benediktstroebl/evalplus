```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This script defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the elements of the input list that contain the given substring. The script uses the fact that the list of strings is passed as a parameter and the substring is passed as a separate parameter.