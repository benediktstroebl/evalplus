```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string if x != '']

# Test cases
test_cases = [
    'abc',
    '123',
    '',
    '   ',
    '\n'
]

for test_str in test_cases:
    actual_prefixes = all_prefixes(test_str)
    assert len(actual_prefixes) == len(expected_prefixes)
    expected_prefixes = ['a', 'ab', 'ac', '123', ' ', '\n']
    for exp, act in zip(expected_prefixes, actual_prefixes):
        assert exp == act, f"For input: {test_str}, expected '{exp}', but got '{act}'"
``` 
This code defines a function `all_prefixes` that returns a list of prefixes from the input string. The function uses a string and an list comprehension to generate all prefixes. The code also includes a list of test cases, which are passed to the function to test its correctness. The test is then run for each test case, comparing the actual result against the expected result.