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
    # Create a set to store unique elements from the list
    unique_elements = set()

    # Iterate over each element in the list
    for num in l:
        # Check if the negative of the current element is already in the set
        if -num in unique_elements:
            # If it is, return True because we've found two distinct elements that sum to zero
            return True
        # Otherwise, add the current element to the set
        unique_elements.add(num)

    # If we've iterated over the entire list and found no pairs of distinct elements that sum to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that solves the problem. The function uses a set to keep track of unique elements from the input list. It iterates over each element in the list, checking if the negative of the current element is already in the set. If it is, the function returns True immediately, because it has found two distinct elements that sum to zero. If the function iterates over the entire list without finding any such pairs, it returns False. The script also includes test cases to verify the correctness of the function.