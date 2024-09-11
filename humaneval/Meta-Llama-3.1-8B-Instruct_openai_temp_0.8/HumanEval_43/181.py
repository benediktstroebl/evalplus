### pairs_sum_to_zero Function
```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    seen = set()  # Dictionary to store elements that have been seen

    for num in lst:
        complement = -num  # The complement of a number is the value that would be needed to sum to zero
        if complement in seen:  # If the complement is in the seen set, then we've found a pair that sums to zero
            return True
        seen.add(num)  # Add the current number to the seen set

    return False  # If we've iterated through the entire list and haven't found a pair, then there is no pair that sums to zero
```
### Example Usage
```python
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```