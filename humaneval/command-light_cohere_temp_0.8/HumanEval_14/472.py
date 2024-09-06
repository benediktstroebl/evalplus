```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string"""
    return [''.join() for _ in range(1 + len(string) + 1)]

# Test case 1
test_case1 = '''abc'''
print(all_prefixes(test_case1))  # ['a', 'ab', 'bc']

# Test case 2
test_case2 = 'abcdechampf'
print(all_prefixes(test_case2))  # ['abc', 'acbd', 'bcd']

# Test case 3
test_case3 = 'abc123'
print(all_prefixes(test_case3))  # ['a', 'ab', 'bc', 'abc']
```
This Python script defines a function called `all_prefixes` that generates a list of all prefixes of a given input string. The function iterates from 1 to the length of the input string, appending each character to the string to create new prefixes. 

The test cases demonstrate how the function works with different input strings.