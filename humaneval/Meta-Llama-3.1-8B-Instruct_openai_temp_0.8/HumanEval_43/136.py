```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    :param lst: A list of integers
    :return: bool
    """
    seen = set()  # Create a set to store the elements we've seen
    for num in lst:  # Iterate over the list
        complement = -num  # Calculate the complement of the current number
        if complement in seen:  # Check if the complement is in the set
            return True  # If it is, return True
        seen.add(num)  # Add the current number to the set
    return False  # If we've iterated over the entire list without finding a pair, return False

# Example use cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script uses a set to keep track of the elements we've seen so far. For each element in the list, it calculates its complement (the number that would need to be added to it to get zero) and checks if that complement is in the set. If it is, that means we've found two numbers that sum to zero, so we return True. If we've iterated over the entire list without finding any pairs, we return False.