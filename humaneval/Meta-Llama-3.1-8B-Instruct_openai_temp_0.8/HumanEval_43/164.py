### Pairs Sum to Zero
#### Problem Description

This script checks if there are two distinct elements in a given list of integers that sum to zero.

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
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in lst:
        # Check if the complement of the current number (0 - num) is in the set
        if 0 - num in seen:
            # If it is, return True
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Example use cases
if __name__ == "__main__":
    print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
    print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
    print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
    print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
    print(pairs_sum_to_zero([1]))  # False
```

#### Explanation

This script works by iterating over the list and checking if the complement of each number (0 - num) is in the set. If it is, we immediately return True. If not, we add the current number to the set. If we've iterated over the entire list and haven't found a pair that sums to zero, we return False.

This approach has a time complexity of O(n), where n is the length of the list, because we're doing a constant amount of work for each element in the list. The space complexity is also O(n), because in the worst case (when all elements are unique), we'll store all elements in the set.