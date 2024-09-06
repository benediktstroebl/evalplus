```python
def double_the_difference(nums):
    odd_squares = sum(x**2 for x in nums if x % 2 and x >= 0)
    return int(odd_squares)
```

This function calculates the `sum(x**2 for x in nums if x % 2 and x >= 0)`, which is the sum of squares of odd integers up to and including the largest odd number, and then casts the result to an integer using int() function. 

To handle the edge cases when there are no inputs (in which case it returns 0), or when there are no odd numbers in the list (in which case it also returns 0), the function uses the filter statement to generate a generator expression, which only yields values where the condition `x % 2` is true and x is greater than or equal to 0. 

This way, the function ignores negative or non-integer values in the list and returns the correct sum of odd squares. 

Here is a test suite to test the function with various inputs:
```python
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([7, 5, 3, 1, 9]) == 144
    assert double_the_difference([4, 6, 8, 10, -2, 2]) == 184
    assert double_the_difference([]) == 0
    assert double_the_difference([-1, -3, -5, -7, -9]) == 0
```