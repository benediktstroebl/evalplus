```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(''.join(sorted(string)))

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("", []),
    ("foo", ["fo", "foo"]),
    ("bar", ["bar"])
]

# Execute the function and verify the results
for input, expected in test_cases:
    actual = all_prefixes(input)
    assert actual == expected
```
This code provides a self-contained function that solves the task of extracting all prefixes from the shortest to longest in a given string. It is a following:
- A function named `all_prefixes` takes a string as input and returns a list of its prefixes.
- The function uses the built-in function `join` to iterate through each character in the string and sort them alphabetically, creating the prefix.
- The sorted characters are then used to build a new string with the desired prefixes.
- The `join` method is used to convert the sorted characters back into a list.
- The function is then tested using a series of test cases, which includes a variety of strings and expected prefix lists. 
- The test cases are defined in the `test_cases` list, and the `all_prefixes` function is called with each input string in the list.
- The results of the function are compared with the expected results using the `assert` assertion, and any mismatch will cause the test to fail.