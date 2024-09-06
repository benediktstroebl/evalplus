```python
def max_element(l: list):
    """Return maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```

The `max_element` function takes a list `l` as an argument and uses the `max` function to return the maximum value in the list. The function works for both positive and negative numbers and will return the highest value in the list. 

To run the test, you can create a file called `test_max_element.py` and copy the following code:
```python
import max_element

def test_max_element():
    assert max_element.max_element([1, 2, 3]) == 3
    assert max_element.max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```

Then, run the tests using the command `python -m unittest test_max_element`.