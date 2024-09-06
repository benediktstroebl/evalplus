Here's the solution:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The function uses the contains method to check if each string contains the substring. It then returns a filtered list.

Let's break it down with comments and explanations:
```python
# Importing the List typing from the typing module
from typing import List

# Defining a function that filters a list of strings by substring, returning a new list of strings that contain the substring
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    # Using the contains method to check if each string in the input list contains the substring
    return [string for string in strings if string.contains(substring)]
```
This code uses the contains method from the string module to determine if a given string has a substring. It returns a list comprehension containing only the strings from the input list that do contain the substring.