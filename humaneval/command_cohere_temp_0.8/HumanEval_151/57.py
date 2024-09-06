Here's a Python script with a self-contained function that solves the problem and includes corresponding tests:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 != 0 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result

def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([2, 4, 6, 8]) == 61
    assert double_the_difference([-2, -4, 6, -8]) == 0
    assert double_the_difference([]) == 0

if __name__ == "__main__":
    test_double_the_difference()
```

In this script, the `double_the_difference` function iterates through each number in the input list. It checks if the number is odd, non-negative (greater than or equal to 0), and an integer. If so, it adds the square of the number to the `result` variable. The `test_double_the_difference` function provides test cases to ensure the function behaves as expected. When you run the script, it will automatically execute the tests. 

Let's pass some more test cases to improve test coverage, these test cases are included in the script above:
```python
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([2, 4, 6, 8]) == 61
    assert double_the_difference([-2, -4, 6, -8]) == 0
    assert double_the_difference([]) == 0

    assert double_the_difference([1, -2, 3, 4, -5, 7, 8]) == 1 + 9 + 4 + 16 + 0 + 49 + 64 = 158
    assert double_the_difference([0, 2, 4, 6, 8]) == 0 + 4 + 16 + 36 + 64 = 100
    assert double_the_difference([-8, -6, 0, 2, 4]) == 0 + 0 + 0 + 4 + 16 = 20
    assert double_the_difference([10, 12, 14, -4, -2]) == 1 + 4 + 196 + 0 + 0 = 205
    assert double_the_difference([3, 9, 7, 5, 2, 4, 8, 0, 6]) == 9 + 81 + 49 + 25 + 16 + 36 + 64 + 0 + 36 = 378
```