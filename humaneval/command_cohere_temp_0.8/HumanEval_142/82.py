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

The code uses a for loop to iterate through each index and corresponding value in the provided list. The conditionals (`if i % 3 == 0:` and `elif i % 4 == 0 and i % 3 != 0`) handle whether to square or cube each value, respectively. Finally, the squared or cubed values are added to the result variable, which is returned at the end of the function.

This code can be imported and used in another Python file with no dependencies, making it self-contained. It also adheres to the problem's requirement that no changes be made to list entries whose indexes are not multiples of 3 or 4. 

To test this script, you can create a Python file that imports this function and includes test cases, such as:
```python
import sum_squares

# Test Case 1
list1 = [1, 2, 3]
expected_result1 = 6
result1 = sum_squares.sum_squares(list1)

# Test Case 2
list2 = []
expected_result2 = 0
result2 = sum_squares.sum_squares(list2)

# Test Case 3
list3 = [-1, -5, 2, -1, -5]
expected_result3 = -126
result3 = sum_squares.sum_squares(list3)

# Ensure that the function passes all tests
assert result1 == expected_result1
assert result2 == expected_result2
assert result3 == expected_result3
```