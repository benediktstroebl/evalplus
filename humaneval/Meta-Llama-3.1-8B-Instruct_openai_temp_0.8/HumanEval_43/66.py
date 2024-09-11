### Pairs Sum to Zero
#### Problem Description
This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise.
#### Code
```python
def pairs_sum_to_zero(numbers):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    bool: Whether two distinct elements sum to zero.
    """
    seen = set()
    for num in numbers:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Example usage
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
#### Explanation
This solution uses a set `seen` to keep track of the numbers we have seen so far. For each number in the input list, we check if its negation is present in the `seen` set. If it is, we immediately return `True`. If we finish checking all numbers without finding a pair that sums to zero, we return `False`. This approach has a time complexity of O(n), where n is the number of elements in the input list.