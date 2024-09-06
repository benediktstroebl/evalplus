Here's the solution to the problem using Python:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
test_strings = ['abc', 'bacd', 'cde', 'array', 'hello', 'world']
test_substring = 'a'
result = filter_by_substring(test_strings, test_substring)
assert len(result) == 3  # Should be ['abc', 'bacd', 'array']
```

This Python code provides a function `filter_by_substring` that takes a list of strings and a substring as input. It then returns a process of filtering out the strings from the list that contain the given substring, making it useful for extracting specific portions of text from a collection.

The test cases provided in the comment pass the function with the test strings and the substring, and the expected result is printed, which ensures the function's correctness.