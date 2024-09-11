### Pairs Sum to Zero
#### Problem Description
The `pairs_sum_to_zero` function checks if there are two distinct elements in a list that sum to zero.

#### Solution
```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that sum to zero, and False otherwise.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        bool: Whether there are two distinct elements in the list that sum to zero.
    """
    seen = set()  # Use a set to store the numbers we've seen so far
    for num in nums:
        complement = -num  # The complement of a number is the number that, when added to it, sums to zero
        if complement in seen:  # If the complement is in the set, return True
            return True
        seen.add(num)  # Otherwise, add the current number to the set
    return False  # If we've iterated over the entire list and found no such pairs, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to store the numbers we've seen so far. It iterates over the list, and for each number, it checks if its complement (i.e., the number that, when added to it, sums to zero) is in the set. If it is, the function returns True; otherwise, it adds the current number to the set. If we've iterated over the entire list and found no such pairs, the function returns False.