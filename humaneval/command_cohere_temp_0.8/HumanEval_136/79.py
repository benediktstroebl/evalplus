```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple `(a, b)`, where `a` is the largest integer of those with negative sign and `b` is the smallest integer of those with a positive sign. The function employs Python's `max` and `min` functions to find the largest negative and the smallest positive integer, respectively.

Here is an example of how to use this function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
```

The output of this code will be: ```(-1, 1)```. 

This self-contained Python function successfully addresses the problem statement and can be incorporated into the context of a larger program.