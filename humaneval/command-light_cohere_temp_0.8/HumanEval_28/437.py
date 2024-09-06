Here is a Python script that contains a self-contained function that concatenates a list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""

    return ''.join(" ".join(strings))
def test_concatenate() -> None:
    test_list = ["a", "bc", "!", "world"]
    expected = "!".join(test_list)
    assert concatenate(test_list) == expected
``` 
This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The `test_concatenate` function contains a test list with a few elements and uses the `assert` statement to check if the concatenated string produced by the `concatenate` function is equal to the expected result.