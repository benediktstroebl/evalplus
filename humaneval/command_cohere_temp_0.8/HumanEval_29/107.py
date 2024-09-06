```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create a new list by applying an operation to each item in the existing list.

To use the `filter_by_prefix` function, you can call it with a list of strings and a prefix. Here is an example of using this function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
In the example, it returns only the strings that start with the prefix "a", thus resulting in a list that contains 'abc' and 'array'. 

The function returns an empty list if the input list is empty or if no strings in the list start with the given prefix. This is because an empty list is returned when the list comprehension operation `strng.startswith(prefix)` is not true for any string in the list. 

This approach utilizes the `startswith` method, which checks if a string starts with a specified prefix, and the list comprehension, which allows for filtering based on this condition. It provides an efficient and concise solution to filter strings by a given prefix in a list.