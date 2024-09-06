```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The code uses a for loop to iterate through each index and number in the provided list. By using the `enumerate` function, the code can easily get the index of each number, checking if it is a multiple of 3 or 4. Based on these conditions, the code either squares or cubies the number, and accumulates the value to return the sum of all changed numbers. 

To test this code, you can use the following example inputs:
```python
test_list = [1,2,3]
expected_output = 6

test_list = []
expected_output = 0

test_list = [-1,-5,2,-1,-5]
expected_output = -126
```

This is an example of how the code can be tested.

If the output of the sum_squares matches the expected_output for each test case, the function is correctly programmed.