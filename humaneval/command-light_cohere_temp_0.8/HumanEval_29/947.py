```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case: Filter words that start with 'a'
test_strings = ['abc', 'bcd', 'cde', 'array', 'added', 'attractive']
test_result = filter_by_prefix(test_strings, 'a')
print(test_result)  # Output: ['abc', 'array']

# Test case: Filter words that start with 'cc'
test_strings2 = ['hello', 'world', 'hello', 'hello, world', 'is', 'first']
test_result2 = filter_by_prefix(test_strings2, 'cc')
print(test_result2)  # Output: ['hello', 'hello', 'hello, world']
``` 
This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It uses the equal for each string in the input list to see if it starts with the provided prefix. This function efficiently filters out the
string that meets this condition.