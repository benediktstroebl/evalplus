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

The Python script defines a function `largest_smallest_integers` that takes a list `lst` as input. It aims to find the largest negative integer and the smallest positive integer in the list and return them in a tuple `(a, b)`. The script initializes `negative` and `positive` as `None`, used for tracking the largest negative and smallest positive values, respectively. It then iterates through the list, checking for negative and positive integers. If a negative integer is found, it compares it to the current `negative`, updating it if necessary. Similarly, for positive integers, it tracks the smallest one among them. Finally, the function returns a tuple containing the largest negative integer (or `None` if none is found) and the smallest positive integer (or `None` if none is found).