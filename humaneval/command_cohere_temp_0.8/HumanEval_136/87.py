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

The `largest_smallest_integers` function works by initially setting two variables, `negative` and `positive`, to `None.` As the function iterates through the list, it compares the current element `n` to the established variables. 

If `n` is smaller than 0 (negative), the function checks if `negative` is currently `None` or if `n` is greater than the existing `negative`. If either of these conditions is true, `negative` is updated to be `n.` Otherwise, if `n` is greater than or equal to 0 (positive), the function checks if `positive` is `None` or if `n` is less than the existing `positive`. If either condition is met, `positive` is updated to be `n`. 

Finally, the function returns a tuple containing the calculated `negative` and `positive` values. 

The provided example test cases demonstrate the correctness of the function.