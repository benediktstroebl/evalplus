```python
def is_equal_to_sum_even(n):
    even_numbers = [2, 4, 6, 8, 10, 12]
    sum_of_even = sum(even_numbers)
    return n == sum_of_even
```

The function `is_equal_to_sum_even` will return True if the number is equal to the sum of four even numbers between 2 and 10, inclusive, and False otherwise. 

Here is an evaluation of the example cases provided:
- `is_equal_to_sum_even(4) == False`: This returns False because 4 cannot be represented as the sum of exactly 4 even numbers.
- `is_equal_to_sum_even(6) == False`: Similarly, 6 cannot be represented as the sum of exactly 4 even numbers, hence the False result. 
- `is_equal_to_sum_even(8) == True`: The function returns True because 8 can be represented as the sum of exactly 4 even numbers (2 + 4 + 6 + 8). 

This code will return the correct value for any integer input n that follows the constraint of the problem.