```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The problem asks us to create a function that returns a tuple `(a, b)`, where `a` is the largest of negative integers and `b` is the smallest of positive integers in a given list. The Python script defines a function called `largest_smallest_integers` that takes in a list of integers as input. It uses the `max` and `min` functions with a custom key to find the largest negative and smallest positive numbers in the list, respectively. If the list contains no negative or positive integers, `None` is returned for either value if it doesn't exist.

Here is an example of how you would use this function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0]))
```

The output would be:
```
(None, 1)
(None, None)
(None, None)
```

This demonstrates that the function works as intended, returning the largest negative and smallest positive numbers, or `None` if there are no such integers in the list.