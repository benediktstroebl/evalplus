```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test case: Filter strings that start with 'a'
test_strings = ['abc', 'bcd', 'cde', 'array', 'aardvark']
test_result = filter_by_prefix(test_strings, 'a')
print(test_result)  # Output: ['abc', 'array']

# Another test case: Filter strings that start with 'geeks'
test_strings_second = ['geeks123', 'geeks', 'icated', 'geekscast']
test_result_second = filter_by_prefix(test_strings_second, 'geeks')
print(test_result_second)  # Output: ['geeks123', 'geeks']
```
This script defines a function **filter_by_prefix** that takes a list of strings and a prefix as input and returns a new list of strings that start with the specified prefix. The script then demonstrates this use of this function with two test cases, printing the filtered strings to the console.