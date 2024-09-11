```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if a pair of distinct elements in the list sum to zero, False otherwise.
    """
    seen = set()  # Set to store elements we've seen so far
    for num in lst:  # Iterate over the list
        if -num in seen:  # Check if -num is in the set
            return True  # If it is, return True
        seen.add(num)  # Add num to the set
    return False  # If we've iterated over the entire list and found no pairs, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```