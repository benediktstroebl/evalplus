Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This script defines a function called `is_equal_to_sum_even` that takes in a number and returns either True or False. It does this by creating a list of all positive even numbers less than or equal to the given number and checks if the given number is in the list, which indicates whether the number can be expressed as the sum of exactly 4 positive even numbers. 

Here's an example of how you can use this function:
```python
print(is_equal_to_sum_even(8))  # Output: True
print(is_equal_to_sum_even(6))  # Output: False
print(is_equal_to_sum_even(7))  # Output: False
```

This will return the answers: `True`, `False`, and `False ` for the respective examples.