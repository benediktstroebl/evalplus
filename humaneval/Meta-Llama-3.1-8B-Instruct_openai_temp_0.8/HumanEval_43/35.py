### pairs_sum_to_zero Function
```python
def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    seen = set()  # Hash set to store seen elements
    for num in lst:  # Iterate over the input list
        complement = -num  # Calculate the complement (the number that needs to be seen to sum to zero)
        if complement in seen:  # Check if the complement has been seen before
            return True  # If the complement has been seen, return True
        seen.add(num)  # Add the current number to the set of seen elements
    return False  # If no pair of distinct elements sums to zero, return False


# Example use cases
if __name__ == "__main__":
    print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
    print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
    print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
    print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
    print(pairs_sum_to_zero([1]))  # False
```

This script defines the `pairs_sum_to_zero` function which checks if there are two distinct elements in the input list that sum to zero. It achieves this in O(n) time complexity by using a hash set to store seen elements. The function returns True if a pair is found and False otherwise. The example use cases are included to demonstrate the function's behavior.