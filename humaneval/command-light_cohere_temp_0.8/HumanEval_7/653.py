```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]


# Tests
test_cases = [
    [],  # empty list
    ['abc', 'a', '123'],  # string containing substring
    ['abc', 'a', 'b'],  # not containing substring
]

# Test function
def test_filter_by_substring():
    for test_case in test_cases:
        actual_result = filter_by_substring(test_case, 'a')
        assert actual_result == ['abc', 'a', '123'], "Verify: {}"

# Run the tests
test_filter_by_substring()
 ``` 
This code demonstrates a Python script with a self-contained function called `filter_by_substring`. The function filters a list of strings for ones that contain a given substring. It uses the `find()` method to search the substring within each string. The test cases cover the general scenarios: empty list, string containing substring, and not containing the substring.  The test_filter_by_substring() function tests the `filter_by_substring()` function with all the test cases and asserts the expected results.