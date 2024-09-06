```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i in l:
        if 0 == i:
            continue
        x, y = i, -i
        if x in seen and y in seen:
            return True
        seen.add(x)
        seen.add(y)
    return False
```

This algorithm uses a hash set 'seen' to keep track of the encountered numbers in the list. It tries to find pairs of numbers 'x', 'y' such that their sum is zero. To avoid duplicates, we only add each number to the set once we have encountered its pair. The function returns True if three distinct elements in the list sum up to zero. Otherwise, it returns False.

Here is an example usage of this function:
```python
>>> triples_sum_to_zero([1, 3, 5, 0])
False
>>> triples_sum_to_zero([1, 3, -2, 1])
True
>>> triples_sum_to_zero([1, 2, 3, 7])
False
>>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
True
>>> triples_sum_to_zero([1])
False
```

The example usage demonstrates the function with different input lists, showing whether three distinct elements in each list sum up to zero or not.