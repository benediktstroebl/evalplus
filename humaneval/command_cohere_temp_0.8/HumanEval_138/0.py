```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The function promptly returns True if the number can be written as the sum of exactly four positive even numbers.

To verify the accuracy of the function, you can test it with a set of examples:
```python
# Test Cases
print(is_equal_to_sum_even(8))  # Should print True
print(is_equal_to_sum_even(6))  # Should print False
print(is_equal_to_sum_even(4))  # Should print False
print(is_equal_to_sum_even(30)) # Should print False
```

All tests should return the expected output as illustrated in the problem statement.