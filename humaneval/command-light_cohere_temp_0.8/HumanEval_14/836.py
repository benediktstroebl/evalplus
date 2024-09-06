```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string) if char != '.' and i != 0]

# Test case 1
test_cases = [
    "abc",
    "Hello, World!",
    "",
    "aa",
    "!"
]

for test_case in test_cases:
    actual_result = all_prefixes(test_case)
    expected_result = ["", "", "a", "!", "]
    print(f"Test case: {test_case} => Actual: {actual_result}, Expected: {expected_result}")
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string. The function uses a array iteration to traverse the string and checks for every character if it's not whitespace and if the index is not 0, adding the character to the result. The code then has a list of test cases, and it iterates through them, calling the all_prefixes function and comparing the actual result with the expected result. The output will be a print statement that shows the test case and the result.