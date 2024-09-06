```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix.isalpha() or Mi any is a list comprehension that loops over all prefixes of the input string and adds them to a new list.

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('123') == []
    assert all_prefixes('') == []
    assert all_prefixes('123') == ['1', '23']

test_prefixes()
``` 
This script defines a function `all_prefixes` that returns a list of all prefixes in the input string. The function uses a list comprehension with a generator expression, which iterates through all possible prefixes and adds them to the list.

Additionally, the script provides a `test_prefixes` function with several test cases to ensure the correctness of the `all_prefixes` function.