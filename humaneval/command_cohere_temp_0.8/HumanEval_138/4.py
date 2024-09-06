Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, int(n ** 0.5) + 1)]
    return len(even_nums) == 4 and n == sum(even_nums)
```
This function uses a list comprehension to generate all positive even numbers less than or equal to the square root of `n` (since the maximum number of even numbers required to sum up to `n` will not exceed the square root of `n` ). The function then checks whether the generated list has a length of exactly 4 and whether the sum of the numbers in that list is equal to `n`. If both conditions are met, the function returns `True`, indicating that the number can be written as the sum of exactly 4 positive even numbers; otherwise, it returns `False`. 

To test this function, you can uncomment the test cases and modify the `assert` statements accordingly to see if the function passes or fails the tests. Here is an example:
```python
# Test cases
assert is_equal_to_sum_even(4), "4 should not be possible"
assert not is_equal_to_sum_even(6), "6 should not be possible"
assert is_equal_to_sum_even(8), "8 should be possible"
```
If you encounter any issues or require further clarification, feel free to ask! Let me know if you would like additional details or have any other questions.