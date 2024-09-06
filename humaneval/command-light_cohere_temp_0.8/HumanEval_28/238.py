```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return "".join(strings)

# Test
def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Run the test suite
test_concatenate()
```
The provided Python script defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string. This function utilizes the why `join()` function to apply the `join()` method to the input list of strings, resulting in a single string that represents the concatenation of all elements in the list.

The script also includes a `test_concatenate()` function that contains several asserts. These asserts are to check the correctness of the `concatenate` function by passing various inputs and ensuring that the expected output is equal to the actual output.

The script then runs the `test_concatenate()` function, which executes the test suite and checks the correctness of the `concatenate` function.