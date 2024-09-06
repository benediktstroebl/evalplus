```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string() if prefix.isalpha(prefix)] 

# Test case 1: Check for empty string
test_cases = [
    '',  # Should return []
    ' ',  # Should return ['']
    'ab'  # Should return ['ab']
    'abc'  # Should return ['ab', 'bc']
]

# Test case 2: Check for single character
test_cases.different strings = ['a', 'abc']

# Test case 3: Check for multiple characters
test_cases. strings strings = ['ab', 'abc']

# Test case 4: Check for single proper prefix
test_cases.

# Test case 5: Check for a mix of characters
test_cases. strings strings = ['ab', 'bc', '!' a', 'zab'] 

# Test case 6: Check for more than one space
test_cases. strings strings = [' abc   ', ' abc    ', '   abcd   '] 

# Test case 7: Check for all prefixes
test_cases.

test_cases[:] = all_prefixes('abc')
for test, expected in zip(test_cases, expected_result(test_cases)):
    print(f"Test: { {test} : {expected} = {test}, {expected} == {test_case_result(test, expected)})")

def test_case_result(test: str, expected: List[str]) -> List[str]:
    return [prefix for prefix in test if prefix.isalpha(prefix)]
```

The code defines a function `all_prefixes(string)` that returns a list of all prefixes in the input string. It uses list comprehension and the strings of all prefixes that are not alpha characters. The code then defines a list of test cases and passes them through the `all_prefixes()` function to verify the correctness of the function.