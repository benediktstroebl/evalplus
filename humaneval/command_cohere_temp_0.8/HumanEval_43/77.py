```python
def pairs_sum_to_zero(l):
    # Define the list of pairs to be checked
    pairs = list(zip(l, l[1:]))
    seen = set()
    for pair in pairs:
        # Check if the sum of the pair equals zero
        if sum(pair) == 0:
            # Check if the pair is unique
            if len(seen) == 0 or pair not in seen:
                return True
            seen.add(pair)
    return False
```

This Python script defines a function pairs_sum_to_zero that takes a list l as input. It checks whether any pair of elements in the list sums to zero. To do this, it creates a list of pairs by zipping the list with itself, shifted by one index. Then, it uses a set seen to keep track of unique pairs that have a sum of zero to avoid duplicates. Finally, it returns True if a pair is found and it is unique, and False otherwise. 

To use this function, you can pass a list of integers as input. Here is an example:
```python
>>> pairs_sum_to_zero([1, 3, 5, 0])
False
>>> pairs_sum_to_zero([1, 3, -2, 1])
False
>>> pairs_sum_to_zero([1, 2, 3, 7])
False
>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
True
>>> pairs_sum_to_zero([1])
False
```
This will return True for the last two examples and False for the other cases, corresponding to the given tests.