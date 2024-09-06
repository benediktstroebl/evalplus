```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.a if prefix not in 'abcadefghijkmnosstooks']

# Test cases
test_cases = [
    'abc',
    '123',
    'a',
    'a123',
    'cotacotao',
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    assert len(actual_prefixes) == 4
    print(f"Test case: {test_case}, Actual: {actual_prefixes}, Expected: {[prefix for prefix in 'abcadefghijkmnosstooks']}")
``` 
The above code defines a function called `all_prefixes` that returns a list of all prefixes from the shortest to the longest of the input string, excluding 'abc', 'adef', 'ghij', 'knosstooks', and any other characters. The function is tested by passing all the test cases and verifying if the output matches the expected prefix list from the corresponding test case.