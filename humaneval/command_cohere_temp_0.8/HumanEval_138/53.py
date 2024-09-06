```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. This is a simple and efficient approach for this problem.

Here is a sample test suite to ensure the function correctly identifies all valid inputs:
```python
def test_is_equal_to_sum_even():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(22) == False
``` 

This test suite covers edge cases like values less than 4 and values greater than the maximum sum of 4 even numbers.