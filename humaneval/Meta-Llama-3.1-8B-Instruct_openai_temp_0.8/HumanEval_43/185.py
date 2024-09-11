```markdown
### Pairs Sum to Zero

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
    """
    seen = set()
    for num in lst:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation

This script uses a set to keep track of the numbers we've seen so far. We iterate over the list, and for each number, we check if its negation is in the set. If it is, we return True, because we've found two numbers that sum to zero. If we finish iterating over the list without finding such a pair, we return False.

This solution has a time complexity of O(n), where n is the length of the list, because we're doing a constant amount of work for each element in the list. The space complexity is also O(n), because in the worst case (when all numbers are different), we might need to store all numbers in the set.