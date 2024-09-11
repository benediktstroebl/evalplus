```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()  # Initialize an empty set to store seen numbers
    for num in nums:
        complement = -num  # Calculate the complement of the current number
        if complement in seen:  # If the complement is in the set, return True
            return True
        seen.add(num)  # Add the current number to the set
    return False  # If no pairs are found, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of seen numbers. It iterates over the input list, for each number it calculates its complement (the number that would sum to zero with it). If the complement is already in the set, it means we've found a pair that sums to zero and the function immediately returns True. If we get through the entire list without finding a pair, the function returns False.