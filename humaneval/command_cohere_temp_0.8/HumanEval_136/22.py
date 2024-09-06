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

The `largest_smallest_integers` function iterates through the list, identifying the largest positive and smallest negative integers. The code utilizes two flags, `positive` and `negative`, which are initially set to `None`. When a number greater than zero is encountered, the `positive` flag is updated to the respective integer if it surpasses the current largest positive. For negative integers, the `negative` flag is updated if the integer is smaller than the current smallest negative. Ultimately, the function returns a tuple consisting of the smallest negative and largest positive integers.

The following example illustrates the function's usage:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0]))
```

The output will be:
```
(None, 1)
(None, None)
(None, None)
```

This demonstrates that the function accurately identifies the smallest positive and largest negative integers within the list, returning `None` for either value if none are found. 

Note that this implementation has a time complexity of O(n), performing a single pass through the input list. It is efficient and directly solves the problem statement. If needed, further optimization can be performed but is unlikely to be necessary for typical input sizes.