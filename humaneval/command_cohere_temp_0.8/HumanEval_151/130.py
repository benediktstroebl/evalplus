```python
def double_the_difference(nums):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in nums:
        if isinstance(num, int) and num % 2 != 0 and num >= 0:
            result += num ** 2
    return result
```

The function `double_the_difference` calculates the sum of squares of odd non-negative integers in the list. It uses a loop to iterate through each number in the input list, checking if the number is an integer, odd, and non-negative. If a number meets these criteria, its square is calculated and added to the result. The function returns the final sum of these squares.

This approach ensures that the function handles negative numbers, non-integer values, and empty input lists gracefully, providing the correct output for the given problem.