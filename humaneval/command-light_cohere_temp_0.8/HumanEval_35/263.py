```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(my_list)
assert result == 123, "Error: Expected maximum element 123, but got " + str(result)

# Test case 2
my_list2 = [5, -5, -10]
result2 = max_element(my_list2)
assert result2 == -5, "Error: Expected maximum element -5, but got " + str(result2)

# Test case 3
my_list3 = [1, -10, 2, 3]
result3 = max_element(my_list3)
assert result3 == 3, "Error: Expected maximum element 3, but got " + str(result3)
```
This script defines a function `max_element` that calculates and returns the maximum element in the input list. The test cases ensure the other elements of lists are passed to the `max_element` function and their returned values are correctly compared against the expected maximum element. 

The output of the script will be a string with the error messages if any of the tests fail.