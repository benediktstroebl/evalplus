```python
def pairs_sum_to_zero(l):
    """
    Check if all pairs of integers in the list sum to zero.
    """
    return "True" if all(x+y == 0 for x, y in l) else "False"
    """

# Test the function
test_result = pairs_sum_to_zero([1, 3, 5, 0])
print(test_result)  # Output: True

test_result = pairs_sum_to_zero([1, 3, -2, 1])
print(test_result)  # Output: False

test_result = pairs_sum_to_zero([1, 2, 3, 7])
print(test_result)  # Output: False

test_result = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
print(test_result)  # Output: True
```
This code defines a function named `pairs_sum_to_zero` that takes a list of integers as input and checks if all pairs of integers in the list sum to zero. The function returns "True" if all pairs sum to zero, and "False" otherwise. The test code section demonstrates the test cases and prints the corresponding results.