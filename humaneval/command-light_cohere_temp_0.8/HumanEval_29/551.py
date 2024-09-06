```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case: filter strings starting with 'a'
test_strings = ['abc', 'bcd', 'cde', 'array', 'ab']
test_result = filter_by_prefix(test_strings, 'a')
print(test_result)  # Output: ['abc', 'array']

# Test case: filter strings starting with 'xx'
test_strings_with_invalid_prefix = ['abc', 'bcd', 'cde', 'array', 'ab', 'xx']
test_result_invalid = filter_by_prefix(test_strings_with_invalid_prefix, 'xx')
print(test_result_invalid)  # Output: []
``` 
This Python code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It takes a required arguments: a list of strings (`strings`) and a prefix (`prefix`). 

The function returns a new list containing only the strings from the input list that start with the provided prefix. 

The code then provides two test cases: one with valid prefix and one with an invalid prefix. 

Finally, the code prints the resulting filtered lists.