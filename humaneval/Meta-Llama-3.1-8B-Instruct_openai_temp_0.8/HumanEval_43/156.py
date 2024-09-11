### Solution: pairs_sum_to_zero
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    :param l: A list of integers
    :return: Boolean indicating whether two distinct elements sum to zero
    """
    # Create a set to store unique elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # Check if -num is in the set
        if -num in seen:
            # If it is, return True because we've found two elements that sum to zero
            return True
        # If not, add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and haven't found a pair that sums to zero, return False
    return False

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script uses a set to keep track of the unique elements we've seen so far, allowing us to check in constant time whether a given number's negation is in the set. If we find such a pair, we immediately return `True`. If we finish iterating over the list without finding such a pair, we return `False`.