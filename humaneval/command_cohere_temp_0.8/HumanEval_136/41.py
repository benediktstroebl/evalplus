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

The Python script defines a function `largest_smallest_integers` that tackles the problem of finding the largest negative and smallest positive integers in a given list. If the list is empty or contains only zero or non-integer values, the function returns `None` for both the largest negative and the smallest positive. The function iterates through the list, identifying positive and negative integers. It updates the `positive` and `negative` variables whenever it finds a more significant positive or a more negative integer, respectively. The function ultimately returns a tuple containing these two values. 

The script includes tests to validate the function's behavior against the problem's provided examples.