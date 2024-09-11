```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.

    Args:
    l (list): A list of integers.

    Returns:
    bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    seen = set()  # Create a set to store the elements we've seen so far
    for num in l:
        if -num in seen:  # Check if the negative of the current number is in the set
            return True  # If it is, we've found two numbers that sum to zero
        seen.add(num)  # Add the current number to the set
    return False  # If we've iterated through the entire list and haven't found any pairs, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns True if there are two distinct elements that sum to zero, and False otherwise. It uses a set to keep track of the elements it has seen so far. For each number in the list, it checks if the negative of that number is in the set. If it is, it returns True immediately. If it iterates through the entire list without finding any pairs, it returns False.