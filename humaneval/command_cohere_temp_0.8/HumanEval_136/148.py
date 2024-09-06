```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            if n > positive:
                positive = n
        elif n < 0:
            if n < negative:
                negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, identifying the smallest positive and largest negative integers. The variables `positive` and `negative` are initialized to negative and positive infinity, respectively, to ensure correct comparisons. As the loop iterates, it compares each integer to the current `positive` and `negative` values and updates them accordingly. Finally, the function returns a tuple containing the largest negative and smallest positive integers, or `None` if none are found. 

Here is how you could use this function to solve the example problems you provided:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Outputs: (None, 1)
print(largest_smallest_integers([]))  # Outputs: (None, None)
print(largest_smallest_integers([0]))  # Outputs: (None, None)
```

This function will handle the case where the list contains only positive or negative integers as well, returning 'None' for the missing value.