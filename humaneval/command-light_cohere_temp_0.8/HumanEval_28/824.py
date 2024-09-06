Here's the Python script:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
# Add unit tests using pytest framework
def test_concatenate():
    assert concatenate(['a', 'b', 'c']) == 'abc'
# Run the tests when running this script
pytest test_concatenate()
```
This script provides a function `concatenate` that takes a list of strings and returns the concatenated string. It also includes unit tests using the test cases with `pytest` framework, which ensures the correctness of the `concatenate` function.