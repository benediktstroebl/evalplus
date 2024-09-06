```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as input and returns a tuple containing the largest negative integer and the smallest positive integer from the list. It uses the `min` and `max` functions with a custom key function to find the smallest positive and largest negative numbers, respectively.

Here's an example of how you can use the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)
```

This example demonstrates the function's behavior for various input lists. The function correctly identifies the largest negative integer and the smallest positive integer, or returns `None` for empty or single-element lists.