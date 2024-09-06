Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly returns whether the number n is present in the list of positive even numbers less than or equal to 20, which forms the required sum of exactly 4 positive even numbers.

To test this function, you can create a test case like the one below:
```python
# Testing the is_equal_to_sum_even function
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(6) == False
assert is_equal_to_sum_even(4) == False
```

This would evaluate whether the function `is_equal_to_sum_even` correctly solves the problem.