### Solution

Here is a Python script that solves the problem using the `set` data structure to check for pairs that sum to zero.

```markdown
### pairs_sum_to_zero.py

```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for num in l:
        # Check if the negative of the current number is in the set
        if -num in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    # If no pairs sum to zero, return False
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

### Explanation

This script works by scanning the input list and checking if the negative of each number is already in the set. If a pair is found that sums to zero, the function returns `True`. If the function finishes scanning the list without finding a pair, it returns `False`.

This solution has a time complexity of O(n), where n is the length of the input list, because it uses a set to store unique elements. The space complexity is also O(n), because in the worst case, the set will contain all elements from the input list.