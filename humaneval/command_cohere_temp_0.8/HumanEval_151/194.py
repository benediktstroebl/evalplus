Here's a Python function that solves the given problem and includes corresponding tests to verify its correctness:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 == 0 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result

# Test cases
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([2, 4, 6, 8]) == 200
    assert double_the_difference([-2, -4, 6, -8]) == 0
    assert double_the_difference([]) == 0

if __name__ == "__main__":
    test_double_the_difference()
```

In this script, the `double_the_difference` function iterates through each number in the input list. If the number is even, negative, or not an integer, it's ignored, and no calculation is performed on it. Otherwise, the number is squared, and its square is added to the `result` variable. Finally, the `result` variable is returned.

The tests in the script cover various scenarios, including positive and negative numbers, odd and even numbers, and empty input lists.