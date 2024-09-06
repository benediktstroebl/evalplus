```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The list `even_nums` can be expanded further to ensure the function works for any positive integer as the universe of numbers included. 

**Note:** This approach assumes the given number can be represented as a sum of 4 unique even numbers. If repetition is allowed, further modification would be needed.