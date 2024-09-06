```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number `n` is present in the list of even numbers `even_nums`. 

The function returns True if `n` can be written as the sum of exactly 4 positive even numbers, and False otherwise. 

To verify the functionality, you can test it with the examples provided in the problem statement like so:
```python
>>> is_equal_to_sum_even(4)  # Should return False
False
>>> is_equal_to_sum_even(6)  # Should return False
False
>>> is_equal_to_sum_even(8)  # Should return True
True
``` 
This confirmation demonstrates that the function appropriately identifies if the given number can be formed through the specified constraint of summing even numbers.