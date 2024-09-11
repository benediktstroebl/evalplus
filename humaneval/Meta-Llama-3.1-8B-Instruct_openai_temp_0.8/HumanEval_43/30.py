### pairs_sum_to_zero Function
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if sum of two distinct elements in the list is zero, False otherwise.
    """
    # Create a set from the list for efficient lookups
    num_set = set()
    
    # Iterate over the list
    for num in l:
        # Check if the negative of the current number is in the set
        if -num in num_set:
            # If it is, return True immediately
            return True
        # Add the current number to the set
        num_set.add(num)
    
    # If we've iterated over the entire list and haven't found a pair of numbers that sum to zero, return False
    return False

### Example Usage
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script defines a function `pairs_sum_to_zero` that solves the problem. It iterates over the input list and for each number, checks if its negative is in a set of numbers seen so far. If it finds a pair of numbers that sum to zero, it returns True immediately. If it iterates over the entire list without finding such a pair, it returns False. The example usage at the end demonstrates the function with the provided test cases.