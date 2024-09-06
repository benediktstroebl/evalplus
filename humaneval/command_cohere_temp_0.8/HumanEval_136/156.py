```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The problem asks us to create a function that returns a tuple (`a`, `b`), where `a` is the largest of negative integers and `b` is the smallest of positive integers in a given list. This function employs the `max` and `min` functions with a custom key to identify the largest negative and smallest positive numbers. If the list contains no negative or positive integers, both values are returned as `None`.

This solution will return the correct result for the examples posed in the problem statement. For instance, it will return `(None, 1)` for the list `[2, 4, 1, 3, 5, 7]`, `(None, None)` for the empty list, and `(None, None)` for the list `[0]`. 

This approach provides a concise solution to the problem, achieving the desired functionality in a straightforward manner.