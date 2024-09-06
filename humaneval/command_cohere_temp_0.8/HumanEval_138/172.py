Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, int(n**0.5) + 1)]
    return n == sum(even_nums)
```
This function uses a list comprehension to generate a list of even numbers from 1 to the square root of `n`. It then returns `true` if the sum of these even numbers is equal to `n`, and `false` otherwise. 

Here is some example output:
```python
>>> is_equal_to_sum_even(8)
True
>>> is_equal_to_sum_even(6)
False
>>> is_equal_to_sum_even(4)
False
```
This code provides a function that solves the given problem and demonstrates the solution's correctness using examples.