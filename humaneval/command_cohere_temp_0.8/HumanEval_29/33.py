```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the input prefix. The function leverages list comprehension and the `startswith` method to efficiently filter out the desired strings. 

Here's an example of using the function with a sample input and an expected output:
```python
>>> filter_by_prefix(=['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

This follows the problem statement and demonstrates the function's correct behavior.