```python
def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    mx, mn = max(lst), min(lst)
    return mn if mx - mn == 1 else None
```

The function `next_smallest()` works by first checking if the list is empty or has less than two elements, returning `None` in such cases as there cannot be a second smallest element. Otherwise, it determines the largest and smallest values in the list using the `max()` and `min()` functions, respectively. 

The key insight here is that the second smallest element is either the smallest element itself or it is the smallest element increased by 1. The function checks this condition and returns the smallest element if it is true, or `None` otherwise.

This approach allows the function to operate without the need for additional tools like `sorted()` or conditional statements, thus maintaining a straightforward and efficient implementation.