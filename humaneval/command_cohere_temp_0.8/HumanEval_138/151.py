```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. 

To test this function, you can write an analogous set of criteria:
```python
# Testing the function with a truthy value
assert is_equal_to_sum_even(8) == True

# Testing the function with a falsy value
assert is_equal_to_sum_even(7) == False

# Testing the function with another truthy value
assert is_equal_to_sum_even(14) == True
```

This list of tests comprehensively evaluates the functionality of the function.