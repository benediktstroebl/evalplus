```python
def max_element(lst):
    if not_elements(lst):  # Empty list
        return None
    return max(lst, key=lambda x: x)

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    got = max_element(test_list)
    assert got == expected
```
The code defines a function max_element that returns the maximum element in the input list lst. It also defines a strategy to return the maximum value in a custom way, using the max function with a key function to sort the list. The test_max_element function tests the max_element function with a sample list and asserts that the function correctly calculates the maximum element.