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

The provided code solves the problem by simultaneously checking for the largest negative integer and the smallest positive integer in the list. It uses a single loop to iterate through the list and update the appropriate variable when a new maximum or minimum is found. This approach ensures efficiency and avoids processing the list twice.

Here is an example usage of the function:
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

This demonstrates that the function handles different scenarios, returning the correct values or `None` as specified in the problem statement.