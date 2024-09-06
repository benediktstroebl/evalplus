Below is a Python script with a self-contained function that filters out strings from a given list that do not contain the given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
_s = ['abc', 'bad', 'cdef', 'array', 'hello']
_ss = ['abc', 'abcd', 'cdef', 'hello']
print(filter_by_substring(_s, _ss))
```
This function utilizes the `find()` method, part of the string's Python built-in `re` module, to determine if the given substring exists within a given string. The output is a list containing only those strings that contain the substring. 

This approach is self-contained, and it does not utilize any external Python libraries.