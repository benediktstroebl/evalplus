```python
def pairs_sum_to_zero(numbers):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    bool: True if a pair of distinct elements sum to zero, False otherwise.
    """
    num_set = set()  # Create a set to store the numbers we have seen so far
    for num in numbers:
        complement = -num  # The number that would sum to zero with the current number
        if complement in num_set:  # If we have seen the complement before
            return True  # We have found a pair that sums to zero
        num_set.add(num)  # Otherwise, add the current number to the set
    return False  # If we have iterated over all numbers and not found a pair that sums to zero

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and checks if there are two distinct elements that sum to zero. It uses a set to keep track of the numbers it has seen so far and returns True as soon as it finds a pair that sums to zero, and False otherwise. The test cases at the end ensure that the function behaves as expected.