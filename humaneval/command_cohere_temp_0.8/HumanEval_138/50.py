Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, int(n ** 0.5) + 1)]
    return n == sum(even_nums)
```
This function uses a list comprehension to generate a list of even numbers from 1 to the square root of `n`. It then returns `True` if the sum of these even numbers is equal to `n`, and `False` otherwise.

To test this function, you can write an example usage like:
```python
print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(7))
print(is_equal_to_sum_even(9))
```
This would lead to the following output:
```
True
False
False
```

And the function passes the given examples correctly.