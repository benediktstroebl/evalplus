### Pairs Sum to Zero
#### Problem Description

The problem asks to create a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise.

#### Solution

```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for num in lst:
        # If the negation of the current number is in the set, return True
        if -num in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    # If no pair that sums to zero was found, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation

This solution uses a set called `seen` to keep track of the numbers we have seen so far. We iterate over the input list, and for each number, we check if its negation is in the set. If it is, we return `True` because we have found a pair that sums to zero. If the negation is not in the set, we add the current number to the set. If we finish iterating over the list without finding any pairs that sum to zero, we return `False`.