```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.debug strings if prefix == string[:len(prefix)] for prefix in string]

# Tests
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']

def test_empty_string():
    assert all_prefixes("") == []

def test_long_string():
    assert all_prefixes("a") == ['a']

if __name__ == "__main__":
    test_all_prefixes()
    test_empty_string()
    test_long_string()
```
This script defines a function `all_prefixes` that returns a list of all prefixes in a given string. The function uses a simple list comprehension to extract all prefixes. 

The script also includes three test functions: `test_all_prefixes`, `test_empty_string`, and `test_long_string`, each of which assert the `all_prefixes` function's output for a given input string. 
Finally, the `if __name__ == "__main__":` block ensures that the test functions are executed when the script is run.