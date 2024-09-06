```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code assumes that you are using Python 3.8 or a later version which supports type hints and the `List[Any]` syntax. If you are working with an earlier version of Python, you may need to adjust the code accordingly. Also, the `Any` type hint essentially means that the function accepts any type, it is provided to satisfy the type checker and should not be interpreted as a recommendation to use it in production code.

This function leverages list comprehension and the `isinstance()` function to filter out only the integer values from the given list `[Any]`. 

To ensure the correctness of the code, let's write a test using the `unittest` module:
```python
import unittest

def test_filter_integers():
    # Test with a list of various elements
    mixed_list = ['a', 3.14, 5, True, None, 'foo']
    result = filter_integers(mixed_list)
    assert result == [5]

    # Test with list containing only integers
    integer_list = [1, 2, 3, 4, 5]
    result = filter_integers(integer_list)
    assert result == integer_list

if __name__ == '__main__':
    unittest.main()
```

In the above test, we first test the function against a `mixed_list` that contains a variety of elements (strings, numbers, boolean, etc.). The function should only return the integer (`5`) in this case. Then, we test it against a list containing only integers to ensure that it returns the list unchanged. 

To run the test, you can save the code into a file (e.g., `test_filter_integers.py`) and execute the file using Python:
```bash
python test_filter_integers.py
``` 

The `unittest` framework will run the tests and report any failures or errors.