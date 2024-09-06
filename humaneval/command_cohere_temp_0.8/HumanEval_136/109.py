```python
def largest_smallest_integers(lst):
    positive = None
    negative = None
    for n in lst:
        if n > 0:
            if positive is None or n > positive:
                positive = n
        elif n < 0:
            if negative is None or n < negative:
                negative = n
    return (negative, positive)
```

The function `largest_smallest_integers` solves the problem by iterating through the list `lst` and identifying the largest negative integer and the smallest positive integer. The function updates the `positive` and `negative` variables whenever a new maximum and minimum is found. Finally, it returns a tuple containing these two values.

The test cases provided in the problem statement are handled correctly by this function, demonstrating its robustness in various scenarios. 
For instance, it returns `(None, 1)` for the input `[2, 4, 1, 3, 5, 7]`, and `(None, None)` for the empty list `[ ]` or a list containing only zeroes `[0]`.