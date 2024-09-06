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

The function `largest_smallest_integers` works by setting the initial values of `positive` and `negative` to negative and positive infinity respectively. This is done to simplify the comparison logic, as any integer value will be less than `negative` and greater than `positive` when initially comparing.

For each integer in the list, the function checks if it is greater than zero. If it is, it updates `positive` to be the smallest seen so far. If it's less than zero, it updates `negative` in a similar way. Finally, the function returns a tuple containing these two values, or `None` if no positive or negative integers were found. 

This approach ensures that the correct result is reached in the minimum number of iterations.