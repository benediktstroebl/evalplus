### Pairs Sum to Zero
#### Problem Description

This script checks if there are two distinct elements in a list of integers that sum to zero.

#### Code

```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()  # Store elements we've seen so far
    for num in l:
        if -num in seen:  # Check if the negative of num is in the set
            return True  # If it is, we've found a pair that sums to zero
        seen.add(num)  # Add num to the set
    return False  # If we've iterated over the entire list and found no pair, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation

This script uses a set to keep track of the elements we've seen so far. For each element in the input list, it checks if the negative of that element is in the set. If it is, it means we've found a pair that sums to zero, and the function returns True. If not, it adds the element to the set and continues to the next element. If it iterates over the entire list without finding a pair, it returns False.