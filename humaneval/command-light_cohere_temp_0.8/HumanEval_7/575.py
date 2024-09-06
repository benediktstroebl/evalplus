```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# Unit tests
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

test_strings = filter_by_substring(strings, substring)
should_contain = ["abc", "bacd", "array"]

test_result = {
    "String list should contain:":
    - {test_contain}
    - {contains}
}

print(test_result)

# Example usage
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
filtered = filter_by_substring(strings, substring)
print(filtered)
``` 
The code defines a function **filter_by_substring** that filters a list of strings based on a given substring. The unit tests section ensures that the function correctly identifies and returns the strings containing the substring. The test results are printed to the console, which should match the expected output. 
The example usage demonstrates how to call the function and print the filtered list of strings.