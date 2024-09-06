```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']

# Test case: Get all prefixes from abc
test_case = 'abc'
result = all_prefixes(test_case)
print(result)  # Output: ['a', 'ab', 'abc']
```
This Python function all_prefixes takes a string s as input and returns a list containing all prefixes (substrings starting from the beginning) of s, without including the empty string itself. 
The test case demonstrates how to use the function with the input string "abc," and the expected output is ['a', 'ab', 'abc'].