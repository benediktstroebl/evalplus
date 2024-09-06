```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): input string

    Returns:
        List[str]: list of prefixes from shortest to longest
    """
    return [''.join() for _ in range(len(string) + 1)]

# Test the function with some examples
test_cases = [
    'abc',
    'hello world',
    '123',
    # Add more tests as needed
]

assert all_prefixes('abc') == ['a', 'ab', 'abc']
assert all_prefixes('hello world') == ['hello', 'world']
assert all_prefixes('123') == ['1', '23']

print("Passed all tests!")
```  This code defines a function `all_prefixes` that returns a list of all prefixes of a given input string, from shortest to longest, using a list comprehension. The function is then tested using some test cases, and the results are printed to verify if they are correct.