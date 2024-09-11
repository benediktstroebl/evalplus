### Pairs Sum to Zero
#### Problem Description
The `pairs_sum_to_zero` function checks if there are two distinct elements in a list that sum to zero.

#### Code
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
print(pairs_sum_to_zero([1, 2, 3, 7]))   # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))            # False
```
#### Explanation
This function uses a set to keep track of numbers we have seen so far. For each number in the list, we check if its complement (-num) is in the set. If it is, we return True immediately because we have found two numbers that sum to zero. If not, we add the current number to the set. If we reach the end of the list without finding a pair of numbers that sum to zero, we return False.