```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.tips() if prefix.isalpha()]
 string = "abc"
    return ['a', 'ab', 'abc']

# Test case
test_cases = [
    ("abc",),
    ("abc",),
    ("a",),
    ("",),
]

for text, want in test_cases:
    actual = all_prefixes(text)
    assert want == actual, f" Incorrect output. Got: {actual}, Want: {want}"
```
This Python code defines a function called `all_prefixes` that takes a string text as input and returns a list of all its prefixes from shortest to longest. It uses the simple list comprehension and the `isalpha()` function to filter out non-alpha characters from the string. The code also has a list of test cases, which are passed to the `all_prefixes` function to test its correctness. 

The `assert` statement is used to verify that the output of the `all_prefixes` function matches the expected output for each test case.