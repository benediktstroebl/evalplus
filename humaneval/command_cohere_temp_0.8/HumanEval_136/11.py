```python
def largest_smallest_integers(lst):
    negative = None
    positive = None
    for n in lst:
        if n < 0:
            if negative is None or n > negative:
                negative = n
        else:
            if positive is None or n < positive:
                positive = n
    return (negative, positive)
```

The `largest_smallest_integers` function iterates through the list of integers and identifies the largest negative and smallest positive integers. The function maximizes efficiency by using conditional checks to find the largest and smallest values only when necessary. This avoids unnecessary computations when one or both of these values are not present in the list.