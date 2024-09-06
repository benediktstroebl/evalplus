```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    # Ensure the list is not empty
    if not nums:
        return []

    # Convert the list to a list of strings to be able to extract digits
    num_strings = [str(num) for num in nums]

    # Extract the digit sums and sort the numbers accordingly
    digit_sums = [sum(int(d) for d in num_string if d.isdigit()) for num_string in num_strings]
    sorted_indices = sorted(range(len(digit_sums)), key=lambda i: digit_sums[i])

    # Retrieve the original numbers sorted by digit sum and tiebreaker index
    sorted_nums = [nums[idx] for idx in sorted_indices]
    return sorted_nums
```

This approach converts the input integers to strings to easily extract their digits, summing these digits to rank the numbers, and using the original index as a tiebreaker when necessary. This algorithm avoids unnecessary computations and is efficient for the given problem. Test cases can be added to ensure the function works correctly. 

Let me know if I have missed any important details or if you'd like me to explain any part of the solution in more detail.