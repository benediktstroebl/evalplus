```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers
    
    Returns:
    bool: True if there are two distinct elements that sum to zero, False otherwise
    """
    seen = set()  # a set to store the elements we've seen so far
    for num in l:
        # if the negation of the current number is in the set, return True
        if -num in seen:
            return True
        # otherwise, add the current number to the set
        seen.add(num)
    # if we've iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the elements we've seen so far. For each element in the list, we check if its negation is in the set. If it is, we've found a pair that sums to zero, so we return `True`. If we've iterated over the entire list without finding such a pair, we return `False`.