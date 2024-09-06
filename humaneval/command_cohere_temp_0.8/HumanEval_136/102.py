```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            if n > positive:
                positive = n
        else:
            if n < negative:
                negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, tracking the largest positive and smallest negative integer values as 'positive' and 'negative' using the `float('-inf')` and `float('inf')` constants, respectively. The function returns a tuple with these values, or `None` if there are no positive or negative integers in the list.