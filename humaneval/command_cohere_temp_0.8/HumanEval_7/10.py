```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two parameters: a list of strings called `strings` and a substring parameter called `substring`. The function returns a new list of strings that contains only the strings from the input list that also contain the given substring. This is accomplished using a list comprehension that iterates through each string in the input list and checks if the substring is a subset of that string, and the expression `[s for s in strings if substring in s]` creates a new list with only the strings that contain the substring. 

This solution is efficient since it utilizes Python's built-in list comprehension, which linearly traverses the list and checks each string for the presence of the substring in O(n) time, where n is the length of the substring and the number of strings in the list.