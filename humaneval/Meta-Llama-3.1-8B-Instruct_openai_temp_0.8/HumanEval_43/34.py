```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for num in lst:
        complement = -num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the numbers we've seen so far. For each number in the list, it checks if the number that would make a pair sum to zero (i.e., the negative of the number) is in the set. If it finds such a pair, it immediately returns True. If it gets through the entire list without finding any pairs, it returns False. This solution has a time complexity of O(n), where n is the length of the list.