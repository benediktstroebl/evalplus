```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [p for p in string if p != '' and p not in {'', 'a', 'ab', 'abc'}]

# Test the function with some inputs and expected outputs
test_cases = [
    ("abc"),
    ("abcd"),
    ("123"),
    ("" * 1000),
    ("")
]

expected = [
    ['a', 'ab', 'abc'],
    ['abcd'],
    ['1'],
    [''],
]

for test, expected in zip(test_cases, expected):
    actual = all_prefixes(test)
    assert actual == expected, f"Test '{test}' failed: {actual} != {expected}"
``` 
This code defines a function `all_prefixes(string: str)` that returns a list of all prefixes in a given string, excluding empty strings and predefined prefixes. It uses the particular test by iterating over the characters in the string and checking if each character is not empty and not one of the predefined prefixes.