### Pairs that Sum to Zero
#### Problem Description
This script checks if there are two distinct elements in a list that sum to zero.

#### Code

```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: Whether there are two distinct elements that sum to zero.
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    
    # Iterate over each element in the list
    for num in lst:
        # Check if the negative of the current number is in the set
        if -num in seen:
            # If it is, return True because we've found two numbers that sum to zero
            return True
        # If not, add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found any pairs that sum to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation
This solution works by iterating over each element in the list and checking if its negative is in a set of elements we've seen so far. If we find a pair of numbers that sum to zero, we immediately return True. If we iter over the entire list without finding any such pair, we return False. This approach has a time complexity of O(n) because looking up an element in a set is a constant time operation, and it uses O(n) space to store the set of elements we've seen.