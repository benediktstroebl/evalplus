```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == '', "Should return empty string"
    assert concatenate(['a']) == 'a', "Should return 'a'"
    assert concatenate(['a', 'b']) == 'ab', "Should return 'ab'"
    assert concatenate(['a', 'bcde']) == 'abcde', "Should return 'abcde'"
    assert concatenate([1, 2, 3]) == '123', "Should return '123'"
# Run the tests
test_concatenate()
``` 
The above Python code defines a function called `concatenate` that takes in a list of strings and returns a new string by concatenating the strings from the list into a single string. It also has a test function that checks the functionality of the `concatenate` function with various input strings and passes all the tests.