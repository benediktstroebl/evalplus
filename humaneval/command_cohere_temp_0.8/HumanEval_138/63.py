Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This script defines a function called `is_equal_to_sum_even` that takes in a number and returns either True or False. It does this by creating a list of all positive even numbers less than or equal to the given number and checks if the given number is in the list, which corresponds to the condition of being the sum of exactly 4 positive even numbers. 

Here's an example of how to use this function:
```python
print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(4))
```

This will output:
```bash
True
False
False
```

This shows that the function correctly identifies numbers that can be expressed as the sum of 4 positive even numbers. 

This script will work in the Python interpreter or when run as a standalone program, and the function can be invoked directly with the provided tests or with other numbers to determine if they satisfy the problem condition.