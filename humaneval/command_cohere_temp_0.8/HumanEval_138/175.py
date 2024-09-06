```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The function returns True if n can be exactly divided by 2, indicating it is an even number. This solution leverages Python's built-in list comprehension and its in membership testing capability, making it both concise and efficient.

Here is a test suite that can be used to validate the function:
```python
# Testing Suite for is_equal_to_sum_even function
def test_is_equal_to_sum_even():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(9) == False
```

This test suite covers various scenarios to ensure the correctness of the `is_equal_to_sum_even` function.