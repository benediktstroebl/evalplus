```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that start with the input prefix. The function uses a list comprehension, creating a new list and filtering its elements using the `startswith` string method. 

To test this function, you can use the following code:
```python
Test: filter_by_prefix([], 'a')
[]
Test: filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
Test: filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar')
['array']
```

This tests the function with different use cases, assuring its correctness. 

The code is concise and easy to understand, following Python's standard naming conventions and principles for list comprehension and string methods. It should be compatible with Python 3.5 and later versions.