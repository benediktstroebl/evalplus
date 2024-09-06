```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two parameters: a list of strings called `strings` and a substring parameter called `substring`. The function returns a new list of strings that contains only the strings from the input list that contain the given substring.

The function uses a list comprehension, creating a new list by iterating over each string in the input list, and returning those that match the specified substring. The `in` operator is used to check if the substring is contained in each string in the list. 

This solution is efficient and will output the filtered list immediately, as it doesn't require any additional libraries and uses a simple list comprehension.