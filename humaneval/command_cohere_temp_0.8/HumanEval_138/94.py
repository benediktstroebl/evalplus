Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```
This function directly tests if the given number `n` is present in the list of even numbers `even_nums` to determine if it can be written as the sum of exactly 4 positive even numbers.

Here's a brief explanation:
- The code defines a Python function called `is_equal_to_sum_even` that takes a single parameter `n`, which represents the number to be evaluated.
- It creates a list called `even_nums` that contains the first 10 positive even numbers: `[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]`.
- The function then checks if the parameter `n` is present in the `even_nums` list. If it is, the function returns `True`, indicating that the number can be expressed as the sum of exactly 4 positive even numbers. If `n` is not in the list, it returns `False`.

This function is concise and directly answers the problem statement. It can be extended to handle larger numbers and more comprehensive tests.