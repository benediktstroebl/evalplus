```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
test_cases = [
    ['abc', 'bcd', 'cde', 'd'],
    ['a'],
    ['a', 'bc'],
    ['a', 'bc', 'de'],
    ['array', 'a', 'b', 'cd'],
    ['bcda', 'ab']
]

# Loop through each test case
for idx, test_case in enumerate(test_cases):
    actual_result = filter_by_prefix(test_case, 'a')
    expected_result = [test_case[0],]
    print(f"Test {idx + 1}: {actual_result} vs {expected_result}")
    if actual_result != expected_result:
        print("Error in test:", end=" ")
``` 
This script defines a function called **filter_by_prefix** which filters an input list of strings based on their prefix. It uses the test cases to verify the functionality of the function.