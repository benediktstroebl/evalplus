```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char for char in string if char.isalpha()) for i, i > 0 else ""].

# Test cases
test_cases = [
    'abc',
    'aab',
    '123#abc',
    'hello world',
    'abc123'
]

test_results = []
for test_case in test_cases:
    test_results.append(all_prefixes(test_case))

print(f'All prefixes for "{": ". ".join for". "{'}''.join found:\n{test_results}')
``` 
This script defines a function `all_prefixes` that returns a list of all prefixes of a given string. It uses a string slicing with list comprehension to filter out any alphabetic characters, and joins them into a new string.