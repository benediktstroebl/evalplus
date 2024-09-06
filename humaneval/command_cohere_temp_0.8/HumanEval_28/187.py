```python
# Importing the necessary module
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result

# Unit tests
def test_concatenate_empty_list():
    assert concatenate([]) == ''

def test_concatenate_non_empty_list():
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Inlining the above tests into the script
if __name__ == "__main__":
    test_concatenate_empty_list()
    test_concatenate_non_empty_list()
```

The function `concatenate` iterates over the list of strings and appends each string to a result string. The tests validate the function's behavior against two cases: an empty list and a non-empty list of strings. The `if __name__ == "__main__":` block ensures that the tests run when the script is executed directly but not when it's imported as a module, which is a recommended practice in Python.