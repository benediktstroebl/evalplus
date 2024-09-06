```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

#Test the function
def test_max_element():
    lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst1) == 123

# Test the function with input of different data type
def test_max_element_type():
    lst2 = ["Hello", "world!"];
    assert max_element(lst2) == "world!"
```
The function max_element takes a list as input and returns the maximum element in the list. The function is then integrated into the above test functions, which provide additional tests to verify the correctness of the max_element function.