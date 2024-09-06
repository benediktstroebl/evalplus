```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to check if the max_element function works
def test_max_element(test_list):
    max_element(test_list) == test_list[-1]

# Example list to test the function
[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
```
The function `max_element` in this program accepts a list as input and outputs the list's highest element. The test_max_element function is used to check if the function is working properly, and it accepts a list as input and compares the outcome with the list's last element.

The list [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10] is used as an example list to test the function.