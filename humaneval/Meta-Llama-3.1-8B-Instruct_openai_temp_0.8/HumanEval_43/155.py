```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    seen = set()  # A set to store the elements we've seen so far
    for num in l:  # Iterate over the list
        complement = -num  # Calculate the complement to sum to zero
        if complement in seen:  # If the complement is in the set
            return True  # We've found two distinct elements that sum to zero
        seen.add(num)  # Add the current element to the set
    return False  # If we've iterated over the entire list and found no pair, return False


# Test cases
if not pairs_sum_to_zero([1, 3, 5, 0]):
    print("Test case 1 passed")
if not pairs_sum_to_zero([1, 3, -2, 1]):
    print("Test case 2 passed")
if not pairs_sum_to_zero([1, 2, 3, 7]):
    print("Test case 3 passed")
if pairs_sum_to_zero([2, 4, -5, 3, 5, 7]):
    print("Test case 4 passed")
if not pairs_sum_to_zero([1]):
    print("Test case 5 passed")
```
This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements that sum to zero, and `False` otherwise. It uses a set to keep track of the elements it has seen so far, and returns `True` as soon as it finds a pair that sums to zero. If it iterates over the entire list without finding such a pair, it returns `False`. The script also includes some test cases to verify the correctness of the function.