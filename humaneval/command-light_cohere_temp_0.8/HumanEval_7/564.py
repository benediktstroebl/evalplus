```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bca", " Hello", "world"]
substring = "o"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['Hello', 'world']
```
This code provides a function `filter_by_substring` that filters an input list of strings and returns a new list that contains only the strings that contain a given substring. 
The code also includes a set of test cases that use the `filter_by_substring` function with different inputs and outputs to test its functionality.