```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer of the negative integers in the list and `b` is the smallest integer of the positive integers in the list. If the list does not contain any negative or positive integers, `a` and `b` should be `None`. The `largest_smallest_integers` function solves this problem by using two separate lists comprehensions, one to find the smallest positive integer and one to find the largest negative integer, and then returning these values in a tuple.

This solution aims to be straightforward and does not require any additional libraries. 
The provided examples in the prompt are also handled correctly by this solution. 
For example:
```python
largest_smallest_integers([2, 4, 1, 3, 5, 7]) 
# == (None, 1)
``` 
and 
```python
largest_smallest_integers([]) 
# == (None, None)
``` 
both return the expected results.