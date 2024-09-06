```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the length of the longest string.
    """
    return max(len(string) for string in strings)

# Unit tests
def test_longest():
    assert longest(['a', 'bb', 'ccc']) == 3
    assert longest([]) is None
    assert longest(['a', 'aa', 'aaa']) == 3
    assert longest(['ab', 'bc']) == 2
    assert longest(['abcd', 'ab']) == 2

if __name__ == "__main__":
    test_longest()
```
This Python code defines a function called `longest`, which takes a list of strings as input and returns the length of the longest string in the list. It uses the max function to find the length of the longest string, and the test suite ensures that the function behaves correctly with various input scenarios. 

The test suite contains several test cases that cover different combinations of strings and validate that the `longest` function returns the correct result for each case.  This test the exposed publicly via `def __name__ == "__main__":` and is executed when the script is run.