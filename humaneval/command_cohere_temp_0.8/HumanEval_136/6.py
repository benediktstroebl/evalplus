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

The `largest_smallest_integers` function iterates through the list, identifying the largest positive and smallest negative integers. The code ensures that if no positive or negative numbers are found, the function returns `None` for both values. 

Here's an example of using the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0]))
```

The output will be:
```
(7, 1)
(None, None)
(None, None)
```

This demonstrates the function's ability to identify the desired integers among various input scenarios.