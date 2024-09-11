```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
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
    """
    num_set = set()
    for num in lst:
        complement = -num
        if complement in num_set:
            return True
        num_set.add(num)
    return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))
print(pairs_sum_to_zero([1, 3, -2, 1]))
print(pairs_sum_to_zero([1, 2, 3, 7]))
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
print(pairs_sum_to_zero([1]))
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input. It uses a set to keep track of the numbers it has seen so far. For each number, it checks if its complement (the number that would add up to zero) is in the set. If it finds such a pair, it immediately returns `True`. If it goes through the entire list without finding any such pair, it returns `False`. The test cases are included at the end of the script.