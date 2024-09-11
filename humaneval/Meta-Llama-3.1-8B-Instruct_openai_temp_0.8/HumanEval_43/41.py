```python
def pairs_sum_to_zero(numbers):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        numbers (list): A list of integers.

    Returns:
        bool: Whether there are two distinct elements in the list that sum to zero.
    """
    seen = set()
    for num in numbers:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

Explanation:
- This function `pairs_sum_to_zero` takes a list of integers as input and returns a boolean value.
- We use a `set` called `seen` to keep track of the numbers we've seen so far.
- We iterate over the list of numbers. For each number, we check if its negation is in the `seen` set.
- If we find a pair of numbers that sum to zero, we immediately return `True`.
- If we finish iterating over the list without finding a pair of numbers that sum to zero, we return `False`.