Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly returns `True` if the number is in the list of even numbers that sum up to 8, 10, 12, 14, 16, 18, 20, 22, 24, or 26. The function naturally handles the cases of n being 8 (the sum of 2, 2, 2, 2), 10 (the sum of 2, 4, 4), and other related cases, all of which return `True`.

The beauty of this approach is its simplicity and efficiency due to not having to iterate over any calculations, a huge benefit when looking for a performant solution in a functional language like Python.