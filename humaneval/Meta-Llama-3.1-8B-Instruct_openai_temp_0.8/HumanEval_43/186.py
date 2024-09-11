```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    num_set = set()
    for num in nums:
        if -num in num_set:
            return True
        num_set.add(num)
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Expected: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Expected: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Expected: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Expected: True
print(pairs_sum_to_zero([1]))  # Expected: False
```
This script creates a solution to the problem that runs in O(n) time, where n is the number of elements in the list, by iterating over the list once and using a set to keep track of the numbers we've seen so far. If we find a number's negative in the set, we return True; otherwise, we continue adding numbers to the set until we reach the end of the list, at which point we return False.