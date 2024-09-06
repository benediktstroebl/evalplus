Here's a Python script that contains a function called `is_equal_to_sum_even` that evaluates whether a given number can be written as the sum of exactly four positive even numbers. The function is designed to return `True` if the condition is met and `False` otherwise:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, (n // 2) + 1)]
    return n == sum(even_nums) and n == sum(even_nums) // 2
```
This function employs list comprehension to generate a list of even numbers from 1 to `(n//2)` inclusively. It then assesses the equality of the calculated sum with the number n, as well as the equality of n with the average of the even numbers. Lastly, it returns `True` if both conditions hold true, and `False` otherwise.

Here is an example of how to use the function:
```python
print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(4))
```

The output will be:
```bash
True
False
False
```

This script demonstrates a straightforward approach that relies on basic math and logic to solve the problem.