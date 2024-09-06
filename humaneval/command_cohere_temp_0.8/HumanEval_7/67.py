```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings `strings` and a substring `substring` as input and returns a new list containing only the strings from the input that contain the given substring. This algorithm uses a list comprehension, which is a concise way to create a new list by applying an operation to each item in the existing list. 

The concise nature of this algorithm makes it an efficient solution to this problem. It also provides a clear and easily understandable solution by explicitly mentioning the filtering criteria in the function name, filtering out strings that contain the specified substring. 

This algorithm's functionality aligns with the problem statement by filtering the list of strings based on the given substring and returning only the relevant strings that contain the substring.