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
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Expected output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Expected output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Expected output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Expected output: True
print(pairs_sum_to_zero([1]))  # Expected output: False
```

This script works by iterating over the input list. For each element, it checks if its negation is in the `seen` set. If it is, the function immediately returns `True`, indicating that there's a pair of elements that sum to zero. If the function iterates over the entire list without finding a pair that sums to zero, it returns `False`. The `seen` set is used to keep track of the elements that have been seen so far, allowing the function to efficiently check if a pair exists.