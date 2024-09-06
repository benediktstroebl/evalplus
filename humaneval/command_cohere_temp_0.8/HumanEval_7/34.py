```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input and returns a new list containing only the strings from the input list that contain the given substring. 

The function utilizes list comprehension and a generator expression to filter the list and to check if the substring is present in each string of the list. The condition `if substring in string` returns True if the substring is found in the string, and False otherwise. Only those strings for which the condition is `True` are picked by the list comprehension. 

Such list comprehensions are a Pythonic way to elegantly and concisely accomplish simple filtering and mapping tasks on Python lists. 

This code is relatively efficient, with a time complexity of O(n), where n is the number of strings in the input list. It performs roughly the same number of operations, regardless of the length of the input string, as it only needs to check if the substring is present in each string and not perform any additional computations. 

Note that this approach assumes the substring is a constant-sized small token, and it might not be suitable for showcasing efficient filtering when the substring could be large or extensive. In such cases, depending on the exact specifications, other efficient approaches might be better. 

If you intend to use this function in a broader context, keep in mind that the Python function `filter()` or asynchronous filtering using `asyncfilter()` might be more suitable for large lists and long substrings.  These functions are designed to be more memory-efficient and faster for large lists, especially when the filtering condition might be more complex than a simple `in` expression.