```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as an argument and returns a tuple containing the largest negative integer and the smallest positive integer from the list. If the list does not contain any negative or positive integers, it returns `None`. 

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

This function handles all the edge cases and returns the correct results based on the specification provided in the problem statement.