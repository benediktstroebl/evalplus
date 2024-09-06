```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. 
The function utilizes a `List comprehension` with the `contains` method to achieve this, creating a new list that only includes the strings with the given substring.