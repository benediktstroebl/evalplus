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

# Test cases
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([1, -1, 2, 3, -4, 5, -2]) == 25

if __name__ == "__main__":
    test_double_the_difference()
```

The function `double_the_difference` uses a loop to iterate over each number in the input list. It checks if each number is an integer, odd, and non-negative before adding its square to the result. The test suite includes different input scenarios to verify the function's correctness.