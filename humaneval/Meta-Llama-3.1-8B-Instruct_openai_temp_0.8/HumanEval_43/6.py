```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()  # Using a set for efficient lookups
    for num in l:
        complement = -num  # The complement of a number is the number that would sum to zero
        if complement in seen:  # If we've seen the complement before
            return True  # Then we have a pair that sums to zero
        seen.add(num)  # Add the current number to the set of seen numbers
    return False  # If we've iterated over the entire list without finding a pair that sums to zero

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set `seen` to keep track of the numbers we've seen so far. For each number in the input list, it checks if its complement (the number that would sum to zero) is in the `seen` set. If it is, then we have a pair that sums to zero and the function returns True. If we've iterated over the entire list without finding a pair that sums to zero, the function returns False.