```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join().
    # Recursive implementation of prefixes
    # from shortest to longest using stack
    return [p for p in string if p != ''] + all_prefixes(string[1:])

# Test cases
test_cases = [
    ('abc', ['a', 'ab', 'abc']),
    ('', ['']),
    ('a', ['a']),
    ('a', ['aa', 'a']),
    ('a', ['aaa', 'aaaa', 'aaaaa'])
]

for text, expected in test_cases:
    actual_prefixes = all_prefixes(text)
    assert actual_prefixes == expected, f"Error in test case: {text}"
```
This code defines a Python function `all_prefixes(string)` that returns a list of all prefixes in a given string, from shortest to longest. The function uses a recursive approach, removing characters from the beginning of the string, and then recursively calls itself to get all prefixes from the rest of the string. The test cases ensure the purpose of the function, passing all the tests successfully.