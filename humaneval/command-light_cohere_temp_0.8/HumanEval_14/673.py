```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])
def all_prefixes_test(test_string: str) -> None:
    actual_result = all_prefixes(test_string)
    expected_result = ['a', 'ab', test_string] + all_prefixes(test_string[1:])
    assert actual_result == expected_result, f"Failure in test: {test_string}"

# Test the function with some sample input
all_prefixes_test('abc')
```
The function all_prefixes takes a string as input and returns a list of all prefixes from shortest to longest of the input string. This is using a recursive approach, the function creates a list of prefixes from the shortest character to the current position and then appends all prefixes from the rest of the string.