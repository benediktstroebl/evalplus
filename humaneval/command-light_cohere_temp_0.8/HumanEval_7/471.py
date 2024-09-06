```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

results = filter_by_substring(strings, substring)
print(results)  # Output: ['abc', 'bacd', 'array']

strings = ["hi", "hello world"]
substring = "wo"

results = filter_by_substring(strings, substring)
print(results)  # Output: []
``` 
This Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. The test cases demonstrate the first, the function works as expected, and prints the filtered list containing strings with the substring "a". 

The second test case fails because the substring "wo" is not present in the input strings. The script will throw an error and return an empty list.