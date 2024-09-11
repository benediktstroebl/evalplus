### Solution
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
    l (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    seen = set()  # A set to store unique elements we have seen so far
    for num in l:  # Iterate over the list
        if num * -1 in seen:  # If the negative of the current number is in the set
            return True  # We have found two distinct elements that sum to zero
        seen.add(num)  # Otherwise, add the current number to the set
    return False  # If we have iterated over the entire list and haven't found any pairs, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Should print False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Should print False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Should print False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Should print True
print(pairs_sum_to_zero([1]))  # Should print False
```

### Explanation

This script defines a function `pairs_sum_to_zero` that takes a list of integers `l` as an input. It uses a set `seen` to store unique elements it has seen so far. 

The function iterates over the list. For each number, it checks if the negative of the current number is in the set `seen`. If it is, it means we have found two distinct elements that sum to zero, so the function returns `True`.

If the current number is not in the set `seen`, it is added to the set. This ensures that we only consider each number once.

If we have iterated over the entire list and haven't found any pairs, the function returns `False`.