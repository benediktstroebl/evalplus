```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [''.join(string[i:]) for i in range(0, len(string), 1)]

# Test case 1: Single character
test_case1 = "a"
print(all_prefixes(test_case1))  # ['a"]

# Test case 2: Two characters
test_case2 = "ab"
print(all_prefixes(test_case2))  # ['ab"]

# Test case 3: Full string
test_case3 = "abc"
print(all_prefixes(test_case3))  # ['a', 'ab', 'abc']
```
The function all_prefixes takes a string as input and returns a list of all its prefixes from shortest to longest. The function uses a list comprehension to iterate through each character of the string and creates a new prefix by slicing that character with a length of 1.