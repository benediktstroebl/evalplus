```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create a set to store elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # Check if the negation of the current number is in the seen set
        if -num in seen:
            # If it is, return True because we've found a pair that sums to zero
            return True
        # If not, add the current number to the seen set
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found a pair, return False
    return False

# Test cases
assert not pairs_sum_to_zero([1, 3, 5, 0])
assert not pairs_sum_to_zero([1, 3, -2, 1])
assert not pairs_sum_to_zero([1, 2, 3, 7])
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
assert not pairs_sum_to_zero([1])
```

This script uses a set to keep track of the numbers we've seen so far. For each number in the list, it checks if its negation is in the set. If it is, the function returns True because we've found a pair that sums to zero. If it's not, the function adds the current number to the set. If we've iterated over the entire list without finding a pair, the function returns False.

The set data structure is used because it allows for constant time lookup, making the function efficient even for large lists.