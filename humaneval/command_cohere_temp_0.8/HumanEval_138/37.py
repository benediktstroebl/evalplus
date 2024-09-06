Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly returns `True` if the number is in the list of even numbers that sum up to 8, 10, 12, 14, 16, 18, 20, 22, 24, or 26 and returns `False` otherwise. It does not require any additional import statements or external dependencies. 
The function can be tested like this:
```python
# Testing a True scenario
print(is_equal_to_sum_even(8))
# Output: True

# Testing a False scenario
print(is_equal_to_sum_even(7))
# Output: False
```

Let me know if you need any additional assistance!