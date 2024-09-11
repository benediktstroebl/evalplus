```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.
    
    Args:
        l (list): A list of integers.
    
    Returns:
        bool: Whether there are two distinct elements in the list that sum to zero.
    """
    seen = set()
    
    for num in l:
        # If the negative of the current number is in the set, return True
        if -num in seen:
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

This script defines a function `pairs_sum_to_zero` that takes a list of integers as an input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. It uses a set `seen` to keep track of the numbers we've seen so far, and checks if the negative of the current number is in the set. If it is, we return `True`, otherwise we add the current number to the set. If we've iterated over the entire list and haven't found a pair that sums to zero, we return `False`. The script then includes some test cases to demonstrate the function's behavior.