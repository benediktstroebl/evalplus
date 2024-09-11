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
    seen = set()  # Create a set to store the elements we've seen so far
    
    for num in l:  # Iterate over each number in the list
        complement = -num  # Calculate the complement of the current number
        if complement in seen:  # Check if the complement is in the set
            return True  # If it is, then we've found a pair that sums to zero
        seen.add(num)  # Add the current number to the set
    
    return False  # If we've iterated over the entire list and haven't found a pair, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the elements we've seen so far. For each number in the list, we calculate its complement (the number that needs to be added to it to get zero) and check if it's in the set. If it is, then we've found a pair that sums to zero, and we return True. If we've iterated over the entire list and haven't found a pair, we return False.