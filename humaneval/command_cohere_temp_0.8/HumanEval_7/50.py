```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. This algorithm uses a list comprehension, which is a concise way to create a new list by applying a condition to each element of the existing list. In this case, it iterates over each element `s` in the `strings` list and includes it in the new list only if it contains the `substring` internally using the `in` operator. 

This implementation has an efficiency of O(n) time complexity, where n is the length of the input list since it requires checking each element once, making it suitable for handling large datasets efficiently.