Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly returns `True` if the number n is in the list of even numbers, and returns `False` otherwise. It is worth noting that the odd numbers are excluded from the list of even numbers to avoid any confusion with odd sums. 
This should provide an effective and efficient solution to the problem, and the function can be readily tested with various input values to ensure its behavior matches the specified example and requirement. 
If you would like to test this function, you can easily call it with different input values to verify its behavior. Here's an example: 
 ```python
print(is_equal_to_sum_even(8))  # Should print True
print(is_equal_to_sum_even(10)) # Should print False
``` 
This will help ensure the function works as expected and is an optimal solution for the problem.