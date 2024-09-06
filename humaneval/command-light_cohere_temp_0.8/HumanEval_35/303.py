```python
def max_element(lst):
    if not_positive(lst):  # Check if list is positive or zero
        return float('-inf')  # Return negative infinity if list is zero or negative
    else:
        return max(lst)

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    got = max_element(test_list)
    assert got == expected

def not_positive(lst):
    return all(map(lambda x: x > 0, lst))

# Call test function
test_max_element()
```

This script defines a function max_element that takes a list lst as input and returns the maximum element in the list. It also defines a test_max_element, which tests the correctness of the max_element function with a test list. The script also defines a_positive function that returns True if the list is positive and False if the list is zero or negative.