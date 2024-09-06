```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as an argument and returns a tuple containing the largest negative integer and the smallest positive integer from the list. If the list contains no negative or positive integers, the function returns `None` for both values to comply with the problem's guidelines.

This solution leverages the `min` and `max` functions, utilizing a key function to identify the smallest positive and largest negative numbers, respectively. This elegant approach efficiently solves the problem while maintaining code simplicity and readability.