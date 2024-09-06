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

The Python script defines a function `largest_smallest_integers` that takes a list of integers as input and returns a tuple containing the largest negative integer and the smallest positive integer from the list. If the list contains no negative or no positive integers, respectively, then the corresponding element in the tuple is set to `None`. 

The function initially sets `negative` and `positive` to `None` to serve as placeholders for the largest negative and smallest positive integers, respectively. Then, it iterates through each integer in the input list using a `for` loop. When it encounters a negative integer, it checks if the `negative` variable is `None` or if the current negative integer is larger than the one stored in `negative`. If either condition is met, it updates `negative` to the current integer. Conversely, when a positive integer is encountered, the function checks if `positive` is `None` or if the current positive integer is smaller than the one stored in `positive`. If either condition is met, it updates `positive` to the current integer. Finally, the function returns a tuple of (`negative`, `positive`).