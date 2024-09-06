Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, int(n**0.5) + 1)]
    return len(even_nums) == 4 and n == sum(even_nums)
```
This function uses a list comprehension to generate all the positive even numbers from 2 up to the square root of `n`, and then checks whether the length of this list is exactly 4 and whether the list's sum is equal to `n`. To ensure the list's length doesn't exceed 4, we limit the numbers to those less than or equal to the square root of `n` since improving a number to another equal to or bigger than the square root wouldn't contribute to the sum while maintaining the requirement of exactly 4 even numbers.