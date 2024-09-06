Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, int(n ** 0.5) + 1)]
    return n == sum(even_nums)
```
This function uses a list comprehension to generate a list of even numbers from 1 to the square root of `n`. It then returns `True` if the sum of these even numbers equals `n`, and `False` otherwise.

To test this function, you can add a suite of test cases that covers different scenarios like the ones you provided in the original prompt:
```python
# Test cases
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(6) == False
```
This will ensure that the function behaves as expected for different input numbers.