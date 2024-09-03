```python
def unique_digits(x):
    # Sort list of positive integers without any even digit
    return sorted(x, key=lambda num: (num % 10 != 0))

# Test case 1
test_case1 = [15, 33, 1422, 1]
test_result1 = unique_digits(test_case1)
print("Test case 1:", end=")")
print(test_result1)

# Test case 2
test_case2 = [152, 323, 1422, 10]
test_result2 = unique_digits(test_case2)
print("Test case 2:", end=")")
print(test_result2)

# Test case 3
test_case3 = [6, 1234567890, 123, -4]
test_result3 = unique_digits(test_case3)
print("Test case 3:", end=")")
print(test_result3)
```
The code defines a function called unique_digits that takes a list of positive integers as input. The function sorts the the list of numbers without any even digit, and the sorted list is returned. The test cases are then used to verify the correctness of the unique_digits function.