Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, int(n**0.5) + 1) if x % 2 == 0]
    return len(even_nums) == 4 and sum(even_nums) == n
```
This function uses a list comprehension to generate all positive even numbers from 2 up to the square root of `n`, and checks whether the length of the list is exactly 4 and whether their sum equals `n`. The function returns `True` if both conditions are met, and `False` otherwise. 

To test this function, you can add the following code after the function definition:
```python
# Testing the function
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(6) == False
assert is_equal_to_sum_even(4) == False
```
This will verify that the function `is_equal_to_sum_even` behaves as expected for the given input values.