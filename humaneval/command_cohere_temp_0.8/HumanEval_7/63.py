```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` which takes two parameters: `strings`, a list of strings, and `substring`, a single string. The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, together with an in operator to check if the substring is present in each string in the list.

If given an empty list or an empty substring, this function will return an empty list. Likewise, if all strings in the input list contain the substring, the function will return every string in the list, whereas if none of the strings contain the substring, the result will be an empty list. 

This makes the `filter_by_substring` function a useful tool for filtering lists of strings based on a specific substring criterion, enabling both inclusion and exclusion filtering operations.