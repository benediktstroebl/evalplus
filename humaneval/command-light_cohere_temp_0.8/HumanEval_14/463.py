```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [x for x in string if x != '' and x not in [' ', '\n']]

# Test cases
test_cases = [
    'abc',
    'abc123',
    '',
    '123',
    '# 1234',
    'abc # babc'
]

for test_case in test_cases:
    actual_prefixes(test_case)
    assert actual_prefixes() == [
        'abc',
        'ab',
        'abcd',
        '',
        '1',
    ]
```
This code defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of the input string. It uses list comprehension and filtering character strings that are not empty and are not spaces or newline characters, which are commonly considered as prefixes.  The test cases are provided in the `test_cases` list, and the function is tested against them. The `assert` statement is used to verify the correctness of the function's output and assert the expected results.