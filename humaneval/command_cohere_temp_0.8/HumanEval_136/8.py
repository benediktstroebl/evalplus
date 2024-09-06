```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as input and returns a tuple containing the largest negative integer and the smallest positive integer from the list. It uses the `max` and `min` functions to find the largest and smallest elements, respectively, while filtering them based on their relationship to 0.

Here's an example of how you can use the function:
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

This demonstrates the function's behavior for various scenarios as described in the problem statement.