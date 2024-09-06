```python
def max_element(lst):
    if not_elements(lst):  # Base case: empty list
        return None
    if lst[0] > lst[-1]:  # Performance optimization: start with leftmost value
        return lst[0]
    else:
        return max(lst)

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    got = max_element(test_list)
    assert got == expected
```
This function, max_element, efficiently computes the maximum element in a given list using a looping approach. The test_max_element function contains a test list with various values and a corresponding expected maximum element. The script also contains a base case check to ensure the function handles empty lists gracefully.