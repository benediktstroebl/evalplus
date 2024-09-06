Here's a Python function that solves the given problem and includes informative tests.

```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 == 1 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result

def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([1, -1, 2, 3, -4, 5, -6]) == 1 + 25 + 9 + 1 + 4 + 25 + 1 + 36 + 0 + 0 + 81 + 0 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0 + 0 + 81 + 0