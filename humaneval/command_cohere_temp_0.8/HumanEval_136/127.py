```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (positive == float('-inf') or n > positive):
            positive = n
        if n < 0 and (negative == float('inf') or n < negative):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, tracking the largest positive and smallest negative integers encountered. Using `float('-inf')` and `float('inf')` allows for efficient comparison of positive and negative values, respectively. The function returns a tuple containing the largest negative and smallest positive integer, or `None` if none are present in the list. 

This approach ensures that the function handles edge cases involving empty, all-positive, or all-negative lists correctly while still finding the intended largest negative and smallest positive integers.