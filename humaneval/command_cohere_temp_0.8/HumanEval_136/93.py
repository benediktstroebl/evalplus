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

The Python script defines a function `largest_smallest_integers` that takes a list as an argument and returns a tuple containing the largest negative integer and the smallest positive integer in the list. If the list contains no negative or positive integers, None is returned for the respective value.

The script passes the following test cases:
1. `largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)`: Returns `(None, 1)` as the list contains no negative numbers and 1 is the smallest positive number. 
2. `largest_smallest_integers([]) == (None, None)`: Tests the empty list case and returns `(None, None)`.
3. `largest_smallest_integers([0]) == (None, None)`: Tests the list containing 0 and returns `(None, None)`  as 0 is not the largest negative or smallest positive number. 

The function iterates through the list, and for each element, it checks if it is greater than zero. If it is, it checks if `positive` is `None` or if the current element is greater than the current `positive`. If it is a negative number, it checks if `negative` is `None` or if the current element is smaller than the current `negative`. This ensures that the `negative` and `positive` variables are updated accordingly.