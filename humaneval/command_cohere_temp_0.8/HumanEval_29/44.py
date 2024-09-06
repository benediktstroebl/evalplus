```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that begin with the input prefix. The function uses a list comprehension, which is a concise way to create a new list by applying an operation to each item in the existing list. In this case, the operation is to filter the strings that have a prefix that matches the desired prefix. 

To implement this, the function utilizes Python's `startswith` method, which checks for the presence of the prefix at the beginning of each string in the list and returns a match if the prefix is found at the start of the string. This method makes the code concise and easier to understand, as it eliminates the need for explicit looping and comparison logic.

The function is designed to be compatible with Python's type hinting system, with the `List[str]` parameter indicating that the input `strings` is a list of strings and the `return List[str]` parameter indicating that the function returns a list of strings. Overall, this function provides an efficient and straightforward solution to filter strings by a given prefix.