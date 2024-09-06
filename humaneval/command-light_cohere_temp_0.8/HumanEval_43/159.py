```python
def pairs_sum_to_zero(l):
    """
    Returns True if the list contains two elements that sum to zero, False otherwise.
    """
    list of integers should be passed as a parameter
    """
    # sort the list first to make the check faster
    l.sort()
    unique_pair that sums to zero in the list. The first one is found and the second one is found by its negation
    # each pair is checked against the first, until a match is found
    while len(set(l[0::repetition(1)] + l[1::repetition(1)])) != 1:
        l[0], l[1] = l[1], l[0]
    # Repeat the above two steps until the set of numbers has more than one number
    return True

# test the function
print(pairs_sum_to_zero([1, 3, 5, 0])) # False
print(pairs_sum_to_zero([1, 3, -2, 1])) # False
print(pairs_sum_to_zero([1, 2, 3, 7])) # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # True
```