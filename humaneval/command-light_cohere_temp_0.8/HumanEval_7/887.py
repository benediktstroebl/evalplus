```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
strings = ["abc", "bacd", "cde", "array", " resetting ", " brown"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)

# Test case 2
strings = ["abc", "bacd", "cde", "array"]
substring = ""
result = filter_by_substring(strings, substring)
print(result)
```
The provided code defines a function called **`filter_by_substring`** that filters a list of strings for instances of a given substring. It utilizes a specific to the principle of list comprehension to create a new list containing only the strings from the input list that contain the provided substring. This function is straightforward and self-contained, making it simple to use and understand.