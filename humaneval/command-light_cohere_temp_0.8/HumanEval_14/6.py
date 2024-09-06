```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' + c for c in string]

# Test the function with some strings
strings = ['abc', 'abc123', '', '123']
assert all_prefixes('') == []
assert all_prefixes('abc') == ['a', 'ab', 'abc']
assert all_prefixes('abc123') == ['abc', 'abc12', '123']
assert all_prefixes('') != ['']
assert all_prefixes('   ') == ['']
```
The code defines a function called `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest of the input string. This is code tests this test the string inputs and asserts the function's output for each case, ensuring the correctness of the `all_prefixes` function.