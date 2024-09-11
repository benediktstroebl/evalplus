```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
    l (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    # Create a set to store the elements we have seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # If the negation of the current number is in the set, return True
        if -num in seen:
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we have iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as an input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses a set to keep track of the elements it has seen so far, and it iterates over the input list to find a pair that sums to zero. The test cases at the end of the script demonstrate the function's behavior on various inputs.