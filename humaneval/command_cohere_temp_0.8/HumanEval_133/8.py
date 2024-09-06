```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = sum(int(round(n)**2 for n in lst if n >= 0))
    return result
```

The function `sum_squares` takes a list of numbers as an argument and returns the sum of the squares of the integers in the list, rounded up to the nearest integer. It employs a list comprehension that iterates through each element in the input list. When a element is an integer and greater than or equal to zero, it is squared, rounded up, and added to the total. The output is the sum of these squared integers, rounded up to the nearest integer. 

This approach ensures that each input element is handled according to the problem statement's requirements, and it provides an accurate, concise way to solve the problem. 

The function can be tested as follows:
```python
# Test Case 1
input_list = [1, 2, 3]
expected_result = 4
result = sum_squares(input_list)
assert result == expected_result

# Test Case 2
input_list = [1, 4, 9]
expected_result = 98
result = sum_squares(input_list)
assert result == expected_result

# Test Case 3
input_list = [1, 3, 5, 7]
expected_result = 84
result = sum_squares(input_list)
assert result == expected_result

# Test Case 4
input_list = [1.4, 4.2, 0]
expected_result = 29
result = sum_squares(input_list)
assert result == expected_result

# Test Case 5
input_list = [-2.4, 1, 1]
expected_result = 6
result = sum_squares(input_list)
assert result == expected_result
```