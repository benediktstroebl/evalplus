```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    num_set = set()  # Set to store the elements we've seen so far
    for num in l:
        complement = -num  # The number that would add up to zero
        if complement in num_set:  # If we've seen the complement before
            return True  # Return True immediately
        num_set.add(num)  # Add the current number to the set
    return False  # If we've iterated through the list and haven't found a pair

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the numbers we've seen so far. For each number, we calculate its complement (the number that would add up to zero) and check if it's in the set. If it is, we return True. If we've iterated through the list and haven't found a pair, we return False. The time complexity is O(n) and the space complexity is also O(n) in the worst case.