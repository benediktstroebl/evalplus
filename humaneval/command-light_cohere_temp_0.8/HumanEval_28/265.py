```python
from typing import List
def concatenate(strings: List[str]):
    # initializing empty string to store concatenation
    result = ""
    # concatenating strings
    for s in strings:
        result += s
    return result
# Test cases
strings_list = ["a", "b", "c"]
result_test = concatenate(strings_list)
print(result_test)  # Output: abc

empty_strings = []
result_empty = concatenate(empty_strings)
print(result_empty)  # Output: 

long_strings = ["a", "bc", "123"]
result_long = concatenate(long_strings)
print(result_long)  # Output: abc123
```
The above Python script defines a `concatenate` function that takes a list of strings as an argument and returns the concatenation of those strings as a single string. It also has a test cases to ensure the functionality of the `concatenate` function.