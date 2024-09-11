### Python Script to Check if Two Elements Sum to Zero
```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        nums (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    num_set = set()  # Use a set to keep track of seen numbers
    for num in nums:
        if -num in num_set:  # Check if -num is in the set
            return True
        num_set.add(num)  # Add num to the set
    return False  # If no pairs are found


# Example use cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script uses a set to keep track of seen numbers. It iterates over the list, and for each number, it checks if its negative counterpart is in the set. If it is, it returns `True` immediately. If it finishes checking all numbers without finding a pair that sums to zero, it returns `False`.