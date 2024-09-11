### Solution: Pairs Sum to Zero
#### Problem Description
This script checks if there are two distinct elements in a list that sum to zero.

#### Code
```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    bool: True if two distinct elements sum to zero, False otherwise.
    
    Examples:
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # Create a set to store the elements we have seen so far
    seen = set()
    
    # Iterate over the list
    for num in lst:
        # Check if the negative of the current number is in the set
        if -num in seen:
            # If it is, return True
            return True
        # If not, add the current number to the set
        seen.add(num)
    
    # If we have iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Test the function
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script uses a set to keep track of the elements it has seen so far. It iterates over the list, and for each element, it checks if its negative is in the set. If it is, it returns True, because it has found a pair that sums to zero. If it hasn't found such a pair after iterating over the entire list, it returns False.