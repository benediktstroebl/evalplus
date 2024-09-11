### Pair Sum to Zero Problem Solution

The following Python script solves the problem of finding pairs of distinct elements in a list that sum to zero.

```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    seen = set()  # Create an empty set to store seen elements
    for num in lst:  # Iterate over the list
        if -num in seen:  # Check if the negative of the current number has been seen
            return True  # If the negative has been seen, return True
        seen.add(num)  # Add the current number to the seen set
    return False  # If no pairs sum to zero, return False

# Example usage
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the elements it has seen so far. It iterates over the list and checks if the negative of the current number has been seen. If it has, it means there is a pair of numbers that sum to zero, so the function returns True. If it hasn't seen any pairs that sum to zero after iterating over the entire list, it returns False.