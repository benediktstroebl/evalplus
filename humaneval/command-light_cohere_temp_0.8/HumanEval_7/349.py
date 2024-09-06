Below is a self-contained Python script that defines a function `filter_by_substring` solving the problem of filtering strings for a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases for function
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

The function takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The test cases pass the main function and print the result to the console. The expected output is the list of strings that contain the substring 'a'.