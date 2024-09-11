```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    :param l: A list of integers
    :return: True if two distinct elements sum to zero, False otherwise
    """
    seen = set()  # A set to store the elements we've seen so far
    for num in l:
        # Check if -num is in the set. If it is, we've found a pair that sums to zero.
        if -num in seen:
            return True
        # Otherwise, add num to the set.
        seen.add(num)
    # If we've iterated over the entire list and haven't found a pair, return False.
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns a boolean value indicating whether there are two distinct elements in the list that sum to zero. It uses a set to store the elements it has seen so far, allowing it to check for pairs in constant time. The test cases at the end demonstrate the function's behavior with various inputs.