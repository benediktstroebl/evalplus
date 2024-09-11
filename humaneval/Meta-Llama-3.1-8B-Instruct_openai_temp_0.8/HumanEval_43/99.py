### Pairs Sum to Zero
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
        bool: Whether two distinct elements in the list sum to zero.
    """
    seen = set()  # keep track of elements we've seen so far
    for num in lst:
        complement = -num  # the number that would sum to zero
        if complement in seen:  # if we've seen the complement before
            return True  # we've found two distinct elements that sum to zero
        seen.add(num)  # add the current number to the set
    return False  # if we've iterated through the list without finding a pair, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation

This script uses a set to keep track of elements we've seen so far. We iterate through the list, and for each number, we calculate its complement (the number that would sum to zero). If we've seen the complement before, we've found two distinct elements that sum to zero, so we return True. If we reach the end of the list without finding a pair, we return False.