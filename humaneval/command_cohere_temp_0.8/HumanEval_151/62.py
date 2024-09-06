```python
def double_the_difference(nums):
    odd_sq = sum(x**2 for x in nums if x % 2 and x >= 0)
    return int(odd_sq)
```

This function leverages Python's list comprehension and the `sum()` function to calculate the sum of squares of odd integers in the `nums` list. The conditional statement `x % 2 and x >= 0` ensures that only positive odd numbers are considered, while negatives and even numbers are excluded. The result is then cast to an integer using `int()` to ensure a whole number is returned. 

To ensure robustness, the function handles edge cases such as empty lists and negative numbers gracefully, returning 0 in such scenarios.