```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function, `filter_by_substring`, filters and returns a new list containing only the strings from the input list that contain the given `substring`. 

The function takes two parameters: `strings`, which is a list of strings, and `substring`, which is a string that we want to find in the strings in the input list. 

The function uses the list comprehension to iterate through the input list of strings. The function then creates an new list, `new_strings`, that contains only the strings from the input list that contain the given `substring`. 

Finally, the function returns this new list, which contains only the strings that contain the given substring.