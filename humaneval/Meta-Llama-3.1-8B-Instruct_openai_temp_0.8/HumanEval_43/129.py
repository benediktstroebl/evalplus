```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
        l (list): A list of integers.
    
    Returns:
        bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    seen = set()  # Set to store the elements we've seen so far
    for num in l:
        if -num in seen:  # Check if the complement of the current number is in the set
            return True  # If it is, we've found a pair that sums to zero
        seen.add(num)  # Add the current number to the set
    return False  # If we've iterated over the entire list and haven't found a pair, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the elements it has seen so far. It iterates over the input list, checking if the complement of each number (-num) is in the set. If it is, the script immediately returns True, indicating that a pair of elements sums to zero. If it iterates over the entire list without finding a pair, it returns False.