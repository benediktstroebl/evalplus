### Solution
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if a pair of elements sums to zero, False otherwise.
    """
    seen = set()  # Set to keep track of elements we've seen
    for num in l:  # Iterate over the list
        complement = -num  # Calculate the complement (the number that would sum to zero)
        if complement in seen:  # If we've seen the complement before
            return True  # Then we've found a pair that sums to zero
        seen.add(num)  # Add the current number to the set
    return False  # If we've iterated over the whole list and found nothing, return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. It uses a `set` to keep track of the elements it has seen so far, and iterates over the list to find pairs of elements that sum to zero. The test cases at the end demonstrate the function's behavior with different inputs.