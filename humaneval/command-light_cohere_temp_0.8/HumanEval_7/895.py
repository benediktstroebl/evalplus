Here is a self-contained Python function that filters an input list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the List comprehension and the contains() string method to filter the input list of strings based on whether the substring is present in the string. It provides an clear and concise solution to the problem. You can use this and call this function and pass your list of strings and the substring you want to filter as arguments to the function. 

This solution has all the required code inside, and does not require any external imports or additional operations.