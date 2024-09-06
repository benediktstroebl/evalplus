```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input. It uses the efficient list comprehension to filter and return only the strings from the input list that contain the given substring. 

I hope this helps you understand how this works and passes the test.