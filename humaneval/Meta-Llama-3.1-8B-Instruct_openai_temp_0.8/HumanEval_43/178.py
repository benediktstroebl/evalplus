```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in lst:
        # Check if the complement of the current number is in the set
        if -num in seen:
            # If it is, return True
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the numbers we've seen so far. It iterates over the list, and for each number, it checks if its complement (the number that would sum to zero) is in the set. If it is, it returns True. If it isn't, it adds the current number to the set and continues iterating. If it iterates over the entire list without finding a pair that sums to zero, it returns False.