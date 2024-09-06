```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != ' ' and c.group := ()]
```
# Test case:
test_all_prefixes('abc')  # ['a', 'ab', 'abc']

test_all_prefixes('abcd')  # ['ab', 'ac', 'bd']

test_all_prefixes('  ')  # ['', '  ]

test_all_prefixes('aa')  # ['a']

test_all_prefixes('aab')  # ['ab']
```
This code defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of the input string. You can uncomment the 

 test cases with this function, passing a variety of input strings and asserting the expected output.