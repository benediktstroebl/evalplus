```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This Python code implements a function called `filter_by_substring` that filters a list of strings and returns a new list that contains only the elements that contain a given substring. The function utilizes the `contains` to iterate through the input strings and checks if each element contains the provided substring using the `contains` method. The result is a list comprehension that filters out any elements that do not contain the substring.