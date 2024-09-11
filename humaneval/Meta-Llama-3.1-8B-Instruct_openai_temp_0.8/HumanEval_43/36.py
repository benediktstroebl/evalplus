```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    seen = set()  # Create a set to store the numbers we have seen so far
    for num in l:  # Iterate over the list
        if -num in seen:  # Check if the negative of the current number is in the set
            return True  # If it is, return True because we have found a pair that sums to zero
        seen.add(num)  # Add the current number to the set
    return False  # If we have iterated over the entire list and not found a pair, return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to efficiently store and look up the numbers we have seen so far. For each number, it checks if its negative is in the set. If it is, it means we have found a pair that sums to zero, and the function immediately returns True. If we have iterated over the entire list and not found a pair, the function returns False.