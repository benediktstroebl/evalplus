Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, int(n ** 0.5) + 1)]
    return len(even_nums) == 4 and n == sum(even_nums)
```
This function uses a list comprehension to generate all the positive even numbers from 2 up to the square root of `n`, and then checks whether the length of this list is exactly 4 and whether the sum of these numbers equals `n`. The function returns `True` if both conditions are met, and `False` otherwise. 

To check the functionality of the `is_equal_to_sum_even` function, you can uncomment the corresponding test cases. 

I hope this helps! Let me know if you have any additional questions.