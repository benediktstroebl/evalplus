```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. It's a simple but straightforward way to solve this problem.

Here is a breakdown of the code:
- The function `is_equal_to_sum_even(n)` takes a single argument n, which represents the number we want to evaluate.
- The list `even_nums` contains the positive even numbers from 2 to 20 (inclusive).
- The function returns True if n can be created through the sum of exactly 4 even numbers (present in our even_nums list), and False otherwise.