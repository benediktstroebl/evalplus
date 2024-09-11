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
    seen = set()  # A set to store elements we've seen so far
    for num in l:
        complement = -num  # The complement is the number needed to sum to zero
        if complement in seen:  # If the complement is in the set, we've found a pair
            return True
        seen.add(num)  # Add the current number to the set
    return False  # If we've iterated through the entire list and haven't found a pair, return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the elements we've seen so far. For each element, we check if its complement (i.e., the number needed to sum to zero) is in the set. If it is, we return True, indicating that we've found a pair of distinct elements that sum to zero. If we've iterated through the entire list without finding a pair, we return False.