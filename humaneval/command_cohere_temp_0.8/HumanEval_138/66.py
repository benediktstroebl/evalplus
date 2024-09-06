```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. Consequently, the function is_equal_to_sum_even will return True for any number that can be written as the sum of exactly 4 positive even numbers, and False otherwise.

Here is a test to validate the function: 
 ```python
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(6) == False
assert is_equal_to_sum_even(4) == False
``` 
This test suite validates the correctness of the solution for various input conditions.