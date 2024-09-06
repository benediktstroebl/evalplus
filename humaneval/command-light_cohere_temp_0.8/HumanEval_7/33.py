```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test case: Filtering strings containing 'a'
strings = ['abc', 'bacd', 'cde', 'array', 'adfa']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This Python script defines a function `filter_by_substring` that filters a list of strings for instances containing a given substring. The function iterates through each element in the list and checks if the substring is present, returning the matching strings. 

In the example, it is used to filter the list of strings for containing the substring 'a', and the output will be ['abc', 'bacd', 'array'].