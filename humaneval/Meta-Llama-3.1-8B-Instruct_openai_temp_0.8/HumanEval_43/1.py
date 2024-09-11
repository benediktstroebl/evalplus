```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Parameters:
    l (list): A list of integers.

    Returns:
    bool: Whether two distinct elements sum to zero.

    Examples:
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # Create a set to store the elements we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # Check if the negative of the current number is in the set
        if -num in seen:
            # If it is, return True
            return True
        # If not, add the current number to the set
        seen.add(num)
    
    # If we've iterated over the entire list and found no pair that sums to zero, return False
    return False

if __name__ == "__main__":
    # Test the function with the provided examples
    print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
    print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
    print(pairs_sum_to_zero([1, 2, 3, 7]))   # False
    print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
    print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers and returns `True` if there are two distinct elements that sum to zero, and `False` otherwise. It uses a set to keep track of the elements it's seen so far, and checks if the negative of each element is in the set. If it finds a pair that sums to zero, it immediately returns `True`. If it iterates over the entire list without finding such a pair, it returns `False`. The script then tests the function with the provided examples.