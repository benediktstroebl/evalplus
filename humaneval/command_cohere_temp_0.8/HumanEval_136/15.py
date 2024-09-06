```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (n < positive or positive == float('-inf')):
            positive = n
        if n < 0 and (n > negative or negative == float('inf')):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list `lst`, tracking the largest positive and smallest negative integers encountered. It uses `float('-inf')` and `float('inf')` to represent the minimum and maximum values of integers, respectively. The function then returns a tuple containing the largest negative and smallest positive values, or `None` if none are found in the list. 

This approach ensures that the function handles all the edge cases mentioned in the problem statement.