```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
``` 
The provided Python script defines a function called `filter_by_prefix` that filters a list of strings based on a given prefix. This function takes a using the list `strings` and a string `prefix` as input. It returns a In this `List[str]` sequence, which contains only the strings from the input list that start with the specified `prefix`. The test cases have been added to demonstrate the function's behavior, and the expected output is printed.