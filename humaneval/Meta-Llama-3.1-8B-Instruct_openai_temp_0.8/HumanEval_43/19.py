```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Parameters:
    lst (list): A list of integers.

    Returns:
    bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    seen = set()  # Initialize an empty set to store the elements we've seen so far

    for num in lst:
        if -num in seen:  # Check if the complement of the current number is in the set
            return True  # If it is, return True because we've found a pair that sums to zero
        seen.add(num)  # Add the current number to the set

    return False  # If we've iterated over the entire list and haven't found a pair, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses a set to keep track of the elements it has seen so far, and it checks if the complement of each number (i.e., its negation) is in the set. If it finds a pair that sums to zero, it immediately returns `True`. If it iterates over the entire list without finding such a pair, it returns `False`.