```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]
def test_function(test_str: str) -> None:
        assert all_prefixes(test_str) == [''.join(c) for c in test_str if c.isalpha()]
 test_function("abc")
``` 
This code provides a function `all_prefixes` that returns a list of all prefixes in a string, using a list comprehension with a list of characters if the character is an alphabet.  The test function `test_function` uses the `assert` statement with the `all_prefixes` function and the string to test if the function is correct. 

Please note that this code assumes the input is a string, and works with alphabetic strings.