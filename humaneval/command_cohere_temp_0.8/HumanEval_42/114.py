Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to iterate over each element in the input list `l`, incrementing each value by 1. The incremented values are then stored in the `result` list. Finally, the function returns the `result` list, which contains the elements of the input list incremented by 1. 

You can verify the function's behavior by calling it with different input lists and comparing the results with the expected output. 
For example:
```python
# Test 1
test_list = [1, 2, 3]
expected_result = [2, 3, 4]
result = incr_list(test_list)
assert result == expected_result

# Test 2
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
expected_result = [6, 4, 6, 3, 4, 4, 10, 1, 124]
result = incr_list(test_list)
assert result == expected_result
```
The tests will successfully pass, confirming the correct operation of the `incr_list` function. 
Feel free to add more tests to ensure the function behaves as expected with different input scenarios. 
You can also further customize the script to auto-run tests or include additional problem solutions as needed.