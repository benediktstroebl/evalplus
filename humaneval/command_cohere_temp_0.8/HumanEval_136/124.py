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

The Python script defines a function `largest_smallest_integers` that takes a list as an input and returns a tuple containing the largest negative integer and the smallest positive integer from the list. If the list doesn't contain any negative or positive integers, it returns `None` for both values.

The function initially sets `negative` and `positive` to `None` to accommodate any negative or positive integers. It then iterates through the list, checking for negative integers. If a negative integer is found, it checks if the `negative` variable is `None` or if the current negative integer is larger than the previous one. If either condition is true, it updates `negative` to the current integer. The same process is carried out for positive integers using the `positive` variable.

Finally, the function returns a tuple of `(negative, positive)` containing the largest negative and smallest positive integers, respectively. If the list contains no negative or positive integers, both values will be `None`. 

This solution follows the problem's guidelines and handles various scenarios, correctly identifying the largest negative and smallest positive integers.