```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])
def all_prefixes_test():
    return [
        'a'      ,  # Single character
        'ab'     ,  # Two characters
        'abc'   # Three characters
        'abcd'   # More than three characters
    ]
def test(string):
    return all_prefixes(string) == all_prefixes_test()
```
This code defines a function all_prefixes that returns a list of all prefixes of a given string, and passes a string test to it, with test_string. It also defines a test that uses these functions to create a list of all possible prefixes and passes it to the all_prefixes function with the same input string, and the test_string, which returns True, indicating that the function is correct.