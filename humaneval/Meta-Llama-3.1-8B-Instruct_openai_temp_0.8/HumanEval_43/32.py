### Python Script: pairs_sum_to_zero
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
    seen = set()  # Initialize an empty set to store seen numbers
    for num in lst:  # Iterate over the list of numbers
        if -num in seen:  # Check if the negative of the current number is in the set
            return True  # If it is, return True because we've found a pair that sums to zero
        seen.add(num)  # Otherwise, add the current number to the set
    return False  # If we've iterated over the entire list without finding a pair, return False

# Example use cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script defines the `pairs_sum_to_zero` function, which uses a set to keep track of seen numbers. It iterates over the list of numbers, checking if the negative of the current number is in the set. If it is, it returns True. Otherwise, it adds the current number to the set. If it iterates over the entire list without finding a pair, it returns False. The script includes example use cases to demonstrate the function's behavior.