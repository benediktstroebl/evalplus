```python
def max_element(lst):
    return max(lst)

# Basic test case
assert max_element([1, 2, 3]) == 3

# List with negative and complex numbers
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# List with unique elements
assert max_element([1, 2, 3, 4, 5]) == 5

# List with duplicate elements
assert max_element([1, 2, 3, 3, 4, 5]) == 5
```
The provided Python script defines a function max_element that aims to return the maximum element in a given list. The function utilizes the basic Python's max() function to achieve this purpose. The code also includes a series of test cases to validate the behavior of the max_element function, passing all the tests with different input lists.