```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']

# Test cases
test_cases = [
    'abc',
    '123',
    '',
    'abc123',
    'a',
    'ab',
    'abcd',
    '123abc'
]

for test_case in test_cases:
    print(all_prefixes(test_case)))
``` 
This Python code defines a function called `all_prefixes` that returns a list of all prefixes of a given input string. 

The function uses a list comprehension to iterate over each character in the input string and adds characters that are not spaces to the resulting list of prefixes. 

Additionally, the code provides several test cases to validate the function's behavior.