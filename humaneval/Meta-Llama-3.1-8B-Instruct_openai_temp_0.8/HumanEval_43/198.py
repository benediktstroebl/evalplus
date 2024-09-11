### Python Solution for Pairs Sum to Zero
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
    seen = set()  # Use a set to keep track of elements we've seen
    for num in lst:
        if -num in seen:  # Check if the negative counterpart is in the set
            return True  # If we find a pair, immediately return True
        seen.add(num)  # Add the current number to the set
    return False  # If we've checked all numbers and found no pairs, return False

# Example use cases:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script uses a set `seen` to keep track of the elements we've seen so far. We iterate over the input list, and for each number, we check if its negative counterpart is in the `seen` set. If it is, we immediately return `True`, indicating that we've found a pair of numbers that sum to zero. If we finish checking all numbers without finding a pair, we return `False`.