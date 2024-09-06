Here is a Python script that defines a function called filter_by_substring that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
# Test cases
my_strings = ['abc', 'bacd', 'cde', 'array', 'hello', 'world']
my_substring = 'abc'
result = filter_by_substring(my_strings, my_substring)
print(result)
```

The code defines a function `filter_by_substring` that takes a list of strings and a substring as input parameters. The function uses a filter method to iterate through the list of strings and returns a new list that contains only the strings that contain the given substring. The test case section shows how the code works when the function is called with different lists of strings and substring values.