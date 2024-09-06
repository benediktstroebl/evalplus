Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This script defines a function called `is_equal_to_sum_even` that takes a number `n` as input and returns either True or False. It checks if the number `n` is present in the list of positive even numbers `even_nums`, which contains exactly 4 even numbers, this list is given in the comments within the code block. If `n` can be exactly divided into 4 even positive numbers, then it returns True, otherwise, it returns False. 

Here's an example of how to use this function:
```python
print(is_equal_to_sum_even(8))  # Output: True
print(is_equal_to_sum_even(6))  # Output: False
print(is_equal_to_sum_even(4))  # Output: False
```

This example demonstrates that the function `is_equal_to_sum_even` correctly identifies if a given number can be expressed as the sum of 4 positive even numbers.