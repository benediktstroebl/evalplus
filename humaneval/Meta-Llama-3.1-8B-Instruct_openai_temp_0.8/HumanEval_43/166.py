```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    seen = set()  # Initialize an empty set to store seen numbers
    for num in lst:  # Iterate over the list
        complement = -num  # Calculate the complement of the current number
        if complement in seen:  # If the complement is in the set
            return True  # Return True because we've found a pair that sums to zero
        seen.add(num)  # Add the current number to the set
    
    return False  # If we've iterated over the entire list and haven't found a pair, return False

# Test the function
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the numbers we've seen so far. For each number in the list, it checks if its complement (-num) is in the set. If it is, that means we've found a pair that sums to zero, and we immediately return True. If we get through the entire list without finding a pair, we return False.