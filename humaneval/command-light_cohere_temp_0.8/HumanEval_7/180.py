```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases
strings = ["abc", "bacd", "cde", "array", "text"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)
``` 
This script defines a function called `filter_by_substring` that takes in a list of strings and a substring as input. It returns a  a new list that contains only the strings from the original list that contain the given substring. The test cases verify that the function works correctly for different inputs and provides the expected results.