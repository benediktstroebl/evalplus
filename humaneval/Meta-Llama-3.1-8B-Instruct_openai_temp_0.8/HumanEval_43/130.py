```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: Whether two distinct elements sum to zero.
    """
    seen = set()  # Use a set to store elements we've seen so far
    for num in lst:
        complement = -num  # The complement of a number is what we need to add to it to get 0
        if complement in seen:  # If we've seen the complement before, return True
            return True
        seen.add(num)  # Add the current number to the set
    return False  # If we've iterated over the list and haven't found a pair that sums to 0, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```