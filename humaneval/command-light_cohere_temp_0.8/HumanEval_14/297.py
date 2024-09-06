```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string() if prefix.isalpha(prefix)]

# Test cases
test_cases = [
    'abc',
    'hello world',
    '',
    None,
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    print(f"Test case: {test_case} => {actual_prefixes}")
    print()

print(f"Expected: ['a', 'ab', 'ac'])")
``` 
This Python code defines a function called `all_prefixes` that returns a list of all prefixes in a given string. The function uses a list comprehension with a generator expression to iterate through all prefixes of the input string, and includes only those that are also alpha characters. The code then provides a list of test cases, and runs the `all_prefixes` function on each test case. The actual and expected output for each test case is printed out, to verify that the function is working correctly.