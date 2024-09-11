### Pairs Sum to Zero
#### Problem Description
This script solves the problem of finding two distinct elements in a list of integers that sum to zero.

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
    bool: Whether there are two distinct elements that sum to zero.
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    # Iterate over the list
    for num in lst:
        # Check if the negative of the current number is in the set
        if -num in seen:
            # If it is, return True
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    # If we've iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation
This script uses a set to keep track of the elements we've seen so far. We iterate over the list, and for each element, we check if its negative is in the set. If it is, we return True, because we've found a pair that sums to zero. If not, we add the current element to the set and continue iterating. If we've iterated over the entire list and haven't found a pair that sums to zero, we return False.