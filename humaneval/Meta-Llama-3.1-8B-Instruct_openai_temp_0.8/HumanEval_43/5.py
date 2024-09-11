```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    seen = set()  # Keep track of elements we've seen so far
    for num in lst:
        complement = -num  # The number that would sum to zero with the current number
        if complement in seen:  # If we've seen the complement before
            return True  # We've found two numbers that sum to zero
        seen.add(num)  # Add the current number to the set
    return False  # If we've iterated through the entire list without finding a pair that sums to zero

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that uses a set to efficiently keep track of the elements it has seen so far. It iterates through the list, checking if the complement of each number (i.e., the number that would sum to zero with the current number) has been seen before. If it has, the function immediately returns `True`. If it iterates through the entire list without finding such a pair, it returns `False`. The test cases at the end demonstrate the function's correctness.