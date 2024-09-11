```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    seen = set()
    for num in lst:
        complement = -num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0])) # False
print(pairs_sum_to_zero([1, 3, -2, 1])) # False
print(pairs_sum_to_zero([1, 2, 3, 7])) # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # True
print(pairs_sum_to_zero([1])) # False
```

This script uses a set `seen` to keep track of the numbers we have already encountered. For each number in the list, we check if its complement (-num) is in the set. If it is, we return True because we have found two numbers that sum to zero. If we finish checking all the numbers without finding a pair that sums to zero, we return False.