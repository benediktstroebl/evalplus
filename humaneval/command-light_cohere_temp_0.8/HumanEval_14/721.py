```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c.isalpha()]

def test_function(test_cases: List[str]) -> None:
    for case in test_cases:
        assert all_prefixes(case) == ['a', 'ab', case[0]]*len(case)
        # Make sure all prefixes are there

    return None
# Example usage of the test function
test_function(['abc'])
```
This script defines a function `all_prefixes` that returns a list of all prefixes of a given string. It uses list comprehension and a modern Python feature `isalpha()` to filter out all the alpha characters from the string. 

The `test_function` is a helper function that takes a list of test cases and asserts that the `all_prefixes` function returns the correct result for each test case.  The result usage of the function with an example test case.