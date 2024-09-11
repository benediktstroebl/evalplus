```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    num_set = set()  # Store each number we've seen so far
    for num in nums:
        if -num in num_set:  # Check if the negation of the current number is in the set
            return True  # If it is, we've found a pair that sums to zero
        num_set.add(num)  # Add the current number to the set
    return False  # If we've checked all numbers and haven't found a pair, return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and checks if there are two distinct elements that sum to zero. It uses a set to store each number as it's seen, and for each number, it checks if its negation is in the set. If a pair is found, the function immediately returns `True`. If it checks all numbers and doesn't find a pair, it returns `False`. The test cases are then executed to verify the function works as expected.