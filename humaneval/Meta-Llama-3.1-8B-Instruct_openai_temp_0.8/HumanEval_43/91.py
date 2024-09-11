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
    seen = set()  # Create a set to store the elements we have seen so far
    for num in l:  # Iterate over each number in the list
        if -num in seen:  # Check if the negation of the current number is in the set
            return True  # If it is, we have found two numbers that sum to zero
        seen.add(num)  # If not, add the current number to the set
    return False  # If we have iterated over the entire list without finding two numbers that sum to zero

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the elements we have seen so far. It iterates over each number in the list, and for each number, it checks if its negation is in the set. If it is, we have found two numbers that sum to zero, so we return True. If we have iterated over the entire list without finding two numbers that sum to zero, we return False.