```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if two distinct elements sum to zero, False otherwise.
    """
    # Create a set to store the elements we have seen so far
    seen = set()
    # Iterate over the list of integers
    for num in l:
        # Calculate the complement (the number that would sum to zero)
        complement = -num
        # If the complement is in the set of seen numbers, return True
        if complement in seen:
            return True
        # Otherwise, add the current number to the set of seen numbers
        seen.add(num)
    # If we have iterated over the entire list and not found a pair that sums to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script works by creating a set to store the numbers it has seen so far. It then iterates over the list of integers. For each number, it checks if its complement (the number that would sum to zero) is in the set of seen numbers. If it is, it returns True. If not, it adds the current number to the set of seen numbers. If it has iterated over the entire list and not found a pair that sums to zero, it returns False.