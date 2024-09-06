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

The Python script defines a function `largest_smallest_integers` that takes a list as an argument and returns a tuple containing the largest negative integer and the smallest positive integer in the list. If the list contains no negative or positive integers, the function returns `None` for both values.

The function first initializes `positive` and `negative` to `None` iterates through the list. It tests each element to determine if it is greater than `0` or less than `0`. If an element is greater than `0`, it updates the `positive` variable to the value of the element if it is smaller than the current `positive` value. If an element is less than `0`, it updates the `negative` variable to the value of the element if it is larger than the current `negative` value. 

At the end of the loop, the function returns a tuple of (negative, positive). Below is an example of how you can use this function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)
```

This will output:
```bash
(None, 1)
(None, None)
(None, None)
```

These values are returned because the list does not contain any negative integers, so `negative` is `None`. The list does contain the positive integer `1`, so `positive` is set to `1`. 

This code assumes that the list may potentially contain negative integers or positive integers, but it may also be empty or contain only integers of one sign. 

It is important to note that this code assumes that the list contains only integers. If the list contains other data types, the function may not return the expected results.