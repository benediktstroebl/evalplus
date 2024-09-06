Here is a Python script that contains a self-contained function that filters out strings that do not contain the given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", " Welcome"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)

```
This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. 
The script then passes test cases and prints the resulting list to the console.