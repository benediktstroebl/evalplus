```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for num in l:
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

This script works by iterating over the list and using a set to keep track of the numbers we've seen so far. If we ever find a number that is the negation of a number we've seen before, we return True immediately, because we've found two distinct numbers that sum to zero. If we reach the end of the list without finding such a pair, we return False, because no such pair exists.