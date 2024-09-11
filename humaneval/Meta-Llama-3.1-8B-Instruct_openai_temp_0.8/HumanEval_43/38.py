### pairs_sum_to_zero Function
#### Description
The `pairs_sum_to_zero` function checks if there are two distinct elements in a list that sum to zero.

#### Code
```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    seen = set()
    for num in lst:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(pairs_sum_to_zero([1]))  # Output: False
```

#### Explanation
This function uses a set `seen` to keep track of the elements it has seen so far. It iterates over the list, and for each element, it checks if its negation is in the `seen` set. If it is, it means that we have found two distinct elements that sum to zero, so it returns `True`. If it hasn't found any such pair after iterating over the entire list, it returns `False`. This approach has a time complexity of O(n), where n is the length of the list.