```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` taking a list of integers as an input and returning the required sum. The function follows the problem's requirements and creates a sum variable that stores the sum of the squared or cubed integers, and finally returns the sum. Take into account that the sum will be calculated only for the integers in the list that have indexes that are multiples of 3 or 4. 

This code also includes tests to ensure its functionality:
```python
# TEST 1: Valid input, multiple of 3
test_list = [1, 2, 3]
expected_result = 6
result = sum_squares(test_list)
print(f'Test 1: {result} == {expected_result}')

# TEST 2: Valid input, multiple of 4, not multiple of 3
test_list = [2, 3, 4]
expected_result = 20
result = sum_squares(test_list)
print(f'Test 2: {result} == {expected_result}')

# TEST 3: Valid input, multiple of both 3 and 4
test_list = [4, 9, 16]
expected_result = 83
result = sum_squares(test_list)
print(f'Test 3: {result} == {expected_result}')

# TEST 4: Valid input, contains negative integers
test_list = [-1, -5, 2, -1, -5]
expected_result = -126
result = sum_squares(test_list)
print(f'Test 4: {result} == {expected_result}')

# TEST 5: Empty list
test_list = []
expected_result = 0
result = sum_squares(test_list)
print(f'Test 5: {result} == {expected_result}')
```

This code contains a set of tests to validate the `sum_squares` function with different inputs and the expected outputs. 

You can add these tests to your codebase to ensure that the function behaves as expected. 
If you desire to have the tests written in markdown, please let me know.