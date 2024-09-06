Here's a Python script with a self-contained function that solves the problem and includes corresponding tests:
```python
# The following test cases verify correct behavior of the double_the_difference function
def test_double_the_difference():
    # Case: Only positive odd integers in the list
    assert double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49 = 84

    # Case: List contains only even or negative integers
    assert double_the_difference([-1, -2, 0, 2, 4]) == 0
    assert double_the_difference([0, -2, -4, 8, -10]) == 0

    # Case: List contains a mixture of odd integers, even integers, and negatives
    assert double_the_difference([9, -2, 7, 0, 11, -13]) == 81 + 49 + 0 + 121 + 169 = 388

    # Case: Empty list
    assert double_the_difference([]) == 0

# The double_the_difference function
def double_the_difference(lst):
    odd_numbers = [num for num in lst if num > 0 and num % 2 != 0]
    return sum(num ** 2 for num in odd_numbers if isinstance(num, int))
```

In this script, the `test_double_the_difference` function verifies the behavior of the `double_the_difference` function against the specified test cases. The `double_the_difference` function itself filters out odd positive integers from the input list, squares them, and sums the result. If the list contains only even or negative numbers, or is empty, it returns 0.