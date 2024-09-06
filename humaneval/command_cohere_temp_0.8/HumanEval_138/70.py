```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. Since the problem states that exactly 4 even numbers are required, the number needs to be precisely present once in the sum to evaluate to true. This avoids the need for dynamic programming or stricter condition checking.