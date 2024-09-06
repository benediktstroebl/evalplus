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

The provided Python script defines a function `largest_smallest_integers` that solves the problem as described in the markdown code block. It iterates through the list, identifying the largest negative and smallest positive integers. The function then returns these two values as a tuple. The code includes necessary conditions to handle cases where the list might not contain negative or positive integers, ensuring that the function returns the correct results for these scenarios.