```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call and expected result
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
This code defines a function `filter_by_substring` that takes two arguments: a list of strings `strings` and a substring `substring`. It uses a list comprehension to filter the input strings list, only retaining the elements that contain the specified substring. 
Test cases are defined to ensure the function's correctness. The output will be the expected results for the given inputs.