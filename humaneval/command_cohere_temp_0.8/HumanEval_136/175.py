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

The provided code defines a function `largest_smallest_integers` that solves the problem as described in the markdown code block. It iterates through the list, identifying the largest negative integer and the smallest positive integer, updating the respective variables `negative` and `positive`. The function ultimately returns a tuple containing these two values. If there are no negative or positive integers in the list, it returns `(None, None)`.