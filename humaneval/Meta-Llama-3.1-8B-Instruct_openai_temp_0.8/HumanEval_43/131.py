### pairs_sum_to_zero Function
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        l (list): A list of integers.

    Returns:
        bool: Whether there are two distinct elements that sum to zero.
    """
    seen = set()  # Keep track of elements we've seen so far
    for num in l:
        complement = -num  # The number that would sum to zero with num
        if complement in seen:  # If we've seen the complement before
            return True  # There are two distinct elements that sum to zero
        seen.add(num)  # Add the current number to the set
    return False  # If we've checked all numbers and haven't found a pair that sums to zero
```
You can test this function with the provided examples:
```python
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```