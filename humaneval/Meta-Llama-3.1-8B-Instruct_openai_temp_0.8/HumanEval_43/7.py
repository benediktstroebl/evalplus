```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # Check if the negation of the current number is in the set
        if -num in seen:
            # If it is, return True
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and found no such pair, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```