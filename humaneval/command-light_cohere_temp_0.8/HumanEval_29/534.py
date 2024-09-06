```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]


# Test cases
test_cases = [
    [],
    ['abc', 'bcd', 'cde', 'array'],
    ['a'],
    ['a', 'bc', 'cde', 'array'],
    ['abcde']
]


print("Test Cases:", endswith(test_cases))

for test_case in test_cases:
    print("\n", endswith(test_case))
    result = filter_by_prefix(test_case, 'a'))
    print(result, endswith("\n"))
```
This Python script defines a function called `filter_by_prefix`, which filters a list of strings based on a given prefix. The function takes in two parameters: a list of strings and a prefix. The function then returns a list of strings that start with the given prefix. The test cases are provided, and the function is then tested with those to ensure it is working correctly.