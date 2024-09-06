```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 strings: List[str] = ['abc', 'bacd', 'cde', 'array', 'carbon']
    substring: str = 'a'
    return ['abc', 'bacd', 'array']
```
This Python function named `filter_by_substring` takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. It uses the relevance to the string searching, where each string in the input is compared to the given substring using the `find()` method. This results in a list of strings that contain the substring, which are then returned by the function.