**Pairs Sum to Zero Solution**
=====================================

Below is a Python script that uses a set data structure to solve the problem.

```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    seen = set()  # Initialize an empty set to store the elements we've seen so far
    for num in lst:  # Iterate over the list
        complement = -num  # Calculate the complement of the current number (i.e., the number needed to sum to zero)
        if complement in seen:  # Check if the complement is in the set of seen numbers
            return True  # If it is, return True because we've found two numbers that sum to zero
        seen.add(num)  # Add the current number to the set of seen numbers
    return False  # If we've iterated over the entire list and haven't returned True, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script works by iterating over the input list and for each number, checking if its complement (-num) is in a set of seen numbers. If it is, the script returns True because it's found two numbers that sum to zero. If it hasn't found such a pair after iterating over the entire list, it returns False. The set of seen numbers is used to keep track of the numbers that have been encountered so far, allowing us to efficiently check if a number's complement is in the set.