```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string]
#Tests
def test_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
```  This code defines a function called `all_prefixes` that returns a list of all prefixes in the string. The code also has a `test_prefixes` function that tests the `all_prefixes` function with the string "abc" which should return the expected output. 
The code uses the Python's `assert` statement to check if the function is working as expected.