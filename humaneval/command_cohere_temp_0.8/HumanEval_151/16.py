```python
def double_the_difference(nums):
    """
    Sum of squares of odd numbers in the list, ignoring negatives and non-integers.
    
    Args:
        nums (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if input list is empty or contains only negatives or non-integers.
    """
    result = 0
    for num in nums:
        if num > 0 and isinstance(num, int) and num % 2:
            result += num ** 2

    return result

# Test cases
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0
assert double_the_difference([-1, 0, 1, -2, 3, 2, 0]) == 1 + 9 + 4 + 0 + 9 + 0 + 0 = 20
```

This function sums the squares of odd numbers and ignores elements that are negative or not integers. Thus, it solves the problem statement correctly.