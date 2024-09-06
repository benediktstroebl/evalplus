```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns a list of all prefixes from shortest to longest of the input string """

    # Store all prefixes
    prefixes = []
    i = 0
    while i < len(string):
        if string[i] != string[0]:
            prefixes.append(string[i])
        i += 1
    return prefixes

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"])
    ("hello world", ["hello", "world"])
    ("", [""])
    ("a", ["b", "a"])

test_results = []
for string, expected in test_cases:
    actual_prefixes = all_prefixes(string)
    test_results.append(set(actual_prefixes, expected))

print("Test Results:", test_results)
``` 
This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes. It uses this typing module to add type hints and improve the reliability of the code. 
The function uses an while loop to iterate over the characters of the input string and append each prefix to the list of prefixes. The test cases are defined to test the function's correctness by comparing the actual results with the expected outputs. 
The test results are printed to the console to verify the function's correctness.