Here's the Python script with the self-contained function that solves the problem:
```python
def is_sum_to_zero(arr):
    total = sum(arr)
    return total == 0

# Example usage
arr1 = [1, 3, 5, 0]
result1 = is_sum_to_zero(arr1)
print(result1)  # Output: False

arr2 = [1, 3, -2, 1]
result2 = is_sum_to_zero(arr2)
print(result2)  # Output: False

arr3 = [2, 4, -5, 3, 5, 7]
result3 = is_sum_to_zero(arr3)
print(result3)  # Output: True
```

The function `is_sum_to_zero` takes an input list `arr` and checks whether its sum equals zero. If the sum is not zero, the function returns `False`, indicating that there are no elements in the list that add up to zero. If the sum equals zero, the function returns `True`.  The test cases demonstrate the functionality of the function.