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
    # Create a set to store the elements we have seen so far
    seen = set()
    
    # Iterate over the list
    for num in lst:
        # If the negation of the current number is in the set, return True
        if -num in seen:
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we have iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to store the elements we have seen so far. If we encounter a number that is the negation of a number we have seen before, we return True. If we iterate over the entire list and don't find any such pairs, we return False. The time complexity of this solution is O(n), where n is the length of the input list.