```python
def max_element(lst):
    if not_list(lst):  # Test if input is a list
        raise TypeError("Input must be a list")
    return max(lst)

# Test the function
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_data) == 123

# Test with invalid input
invalid_input = [object()]
with pytest.assert( raises(TypeError, "Input must be a list")) as e:
  max_element(invalid_input)
``` 
The script includes a `max_element` function that takes a list as an argument. The function first checks if the list is given, if not, it raises a `TypeError`. It then returns the maximum element from the list using the `max` function. 

The script also includes two tests: 
1. the first test the using the function with a sample list of numbers and asserts that the result is correct. 
2. The second test with an `None` list, which should raise a `TypeError` with the message "Input must be a list". 
Do let me know if you need any further assistance!