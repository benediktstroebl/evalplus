```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [x for x in string if x != '' and x not in [' ', '.', '\n']]

# Test the function with various strings
test_cases = [
    "abc",
    "Hello World",
    "   ",
    "a",
    "hello world",
    " 极意isease.",
    "Python is great"
]

for test_string in test_cases:
    actual_prefixes = all_prefixes(test_string)
    print(f"Expected: {', ' '.join(test_prefixes)})
    print(f"Actual: {', '.join(actual_prefixes)})
``` 
This code defines a function `all_prefixes` that returns a list of prefixes from the input string. The function uses a list comprehension and a built-in function `str`. The test cases are defined as a list of strings, and the function is tested with each test case.