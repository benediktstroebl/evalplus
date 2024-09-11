```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # Check if the negative of the current number is in the seen set
        if -num in seen:
            # If it is, return True
            return True
        # Otherwise, add the current number to the seen set
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

This script works by iterating over the list and checking if the negative of each number is in a set of numbers we've seen so far. If we find a pair that sums to zero, we return True. If we finish iterating over the list without finding a pair, we return False. 

This solution has a time complexity of O(n), where n is the length of the list, because we're doing a constant amount of work for each number in the list. The space complexity is also O(n), because in the worst case we might need to store every number in the list in the set.