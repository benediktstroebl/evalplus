```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    seen = set()  # Create a set to keep track of elements we have seen so far
    for num in lst:  # Iterate over each number in the list
        complement = -num  # Calculate the complement of the current number
        if complement in seen:  # If the complement is in the set
            return True  # We have found two distinct elements that sum to zero
        seen.add(num)  # Add the current number to the set
    return False  # If we have iterated over the entire list and not found a pair


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of elements we have seen so far. For each number in the list, we calculate its complement (-num) and check if it is in the set. If it is, we have found two distinct elements that sum to zero, so we return True. If we have iterated over the entire list and not found a pair, we return False.