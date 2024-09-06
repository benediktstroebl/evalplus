```python
def max_element(l: list):
    """Return maximum element in the list
    Return the maximum element in the list l."""
    return max(l)
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
The provided Python script defines a function `max_element` that calculates and returns the maximum element in the list. The function utilizes the straightforward Python `max()` function to find the largest element. The `test_max_element` function contains assertions that check if the `max_element` function correctly calculates the maximum element for different input lists.