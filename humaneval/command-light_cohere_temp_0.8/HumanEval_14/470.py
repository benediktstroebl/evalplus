```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join() for i, char in enumerate(string, 1)]

# Test cases
test_cases = [
    'abc',
    'zab',
    'abcabc',
    'Hello, world!',
]

for test_str in test_cases:
    actual_result = all_prefixes(test_str)
    expected_result = ['a', 'ab', 'abc']  # From shortest to longest
    print(f"Test case: {test_str}, {actual_result}, {expected_result}")
    assert actual_result == expected_result
``` 
This code defines a function that returns a list of all prefixes in a given string, from shortest to longest, using a loop. Each test case provides a values to test the function with. The code also prints the both the actual and expected results for each test case and uses the assert statement to check if the actual result matches the expected one.