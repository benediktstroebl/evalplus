### pairs_sum_to_zero Function
#### Description
This function checks if there are two distinct elements in the list that sum to zero.

#### Code

```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if two distinct elements sum to zero, False otherwise.
    """
    seen = set()  # Initialize a set to store seen elements
    for num in l:
        # Calculate the complement to reach zero
        complement = -num
        # Check if the complement has been seen before
        if complement in seen:
            # If it has, return True
            return True
        # If not, add the current number to the seen set
        seen.add(num)
    # If no pairs sum to zero, return False
    return False

# Example use cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

#### Explanation
The `pairs_sum_to_zero` function iterates through the list and checks for each number if its complement (-num) has been seen before. If a complement has been seen before, the function immediately returns True. If no such pair is found after checking all numbers, the function returns False. This approach has a time complexity of O(n), where n is the length of the list.