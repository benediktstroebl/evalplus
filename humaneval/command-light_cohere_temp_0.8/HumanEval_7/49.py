```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Tests
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # ['abc', 'bacd', 'array']
``` 
This code defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The tests section ensures the use of the function with different strings and substring inputs, and the output is printed to the console.