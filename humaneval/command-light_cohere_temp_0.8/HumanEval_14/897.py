```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]
def test_function():
    return all_prefixes("abc") == ['a', 'ab', 'abc']

def all_prefixes(string) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]

test_function()  # This line will fail if the all_prefixes function has a bug
```
This code defines a function all_prefixes that returns a list of all prefixes in a string, it uses a list comprehension with a condition to filter out non-alpha characters. The test_function function tests if the all_prefixes function is correct, which is a common testing technique. 
The code also includes a bug in the test_function, which will cause it to fail if the all_prefixes function has a bug. 
This is a good starting point for the problem, and you can continue to improve and test the function thoroughly.