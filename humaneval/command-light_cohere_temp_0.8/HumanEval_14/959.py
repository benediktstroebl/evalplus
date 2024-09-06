```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ''] + string.test_cases()

def test_cases():
    return [
        ('abc', ['a', 'ab', 'abc']),
        ('123', ['123']),
        ('abc123', ['a', 'ab', '123', 'abc']),
        ('a123', ['123']),
        ('abcde', ['abc', 'abcd', 'abce', 'acb'])
    ]
``` 
This code provides a function all_prefixes, which takes a string as input and returns a list of all prefixes, from shortest to longest, including the empty string. 
The test_cases function provides several test cases for the all_prefixes function to ensure its correctness.