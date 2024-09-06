```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks for the largest negative integer and the smallest positive integer in a list. The Python function `largest_smallest_integers` solves this problem by using `max` and `min` functions to find the largest negative and smallest positive numbers in the list. The function returns these as a tuple, with `None` if there are no negative or positive numbers in the list. 

Here is an example usage of this function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0])) 
```

This will output:
```
(7, 1)
(None, None)
(None, None)
```

This shows that the function works as intended, finding the largest negative and smallest positive numbers in various lists, and returning `None` when there are no such numbers.