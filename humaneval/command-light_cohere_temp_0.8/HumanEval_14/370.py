```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(). string() for _ in range(len(string), 1, -1)]

# Test cases
test_cases = [
    'abc',
    '123',
    '',
    '::',
    'abc123',
    'abc123_',
    'ABC123_',
]

for case in test_cases:
    actual = all_prefixes(case)
    print(f'Expected: {', [case[i] for i in actual]})
``` 
This code defines a function all_prefixes that returns a list of all prefixes of a given string. The function uses the important to iterate through all characters of the string in all possible orders from shortest to longest, which is achieved using a for loop and the range function. The test cases are also defined and passed to the function to test if it is working correctly.