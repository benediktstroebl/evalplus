```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hi"]
substring = "a"

# Function call and test results
print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']
```
This code implements a function called `filter_by_substring` that takes two parameters: a list of strings `strings` and a substring `substring`. It returns a new list containing elements of the input list that contain the given substring. The code is an test case to pass various strings and substring values and prints the resulting filtered list to the console.