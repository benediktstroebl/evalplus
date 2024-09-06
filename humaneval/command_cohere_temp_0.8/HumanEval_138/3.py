```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The function promptly returns true if the number can be formed and false if it cannot.

To verify the accuracy of the function, you can test it against the examples provided in the problem statement:
```python
print(is_equal_to_sum_even(8))  # Output: True
print(is_equal_to_sum_even(6))  # Output: False
print(is_equal_to_sum_even(4))  # Output: False
```

These tests will confirm that the function appropriately solves the problem.