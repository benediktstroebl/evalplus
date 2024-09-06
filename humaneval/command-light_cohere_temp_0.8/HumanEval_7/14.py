```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function with different inputs
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
The code defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. The code then demonstrates the specific inputs and passes the test by printing the result.