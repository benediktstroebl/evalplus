### pairs_sum_to_zero Function
#### Python Script

```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for num in lst:
        # Check if the complement of the current number exists in the set
        if -num in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    return False

# Example usage
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set, `seen`, to keep track of the numbers we've seen so far. For each number `num` in the input list `lst`, it checks if `-num` (the complement of `num`) exists in the `seen` set. If it does, it means we've found a pair of numbers that sum up to zero, so we return `True`. If not, we add `num` to the `seen` set and continue to the next number. If we've processed the entire list without finding a pair, we return `False`.