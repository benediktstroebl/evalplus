```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest higher integer first.
    """
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

This Python script defines a function called `sum_squares` which takes in a list of numbers (`lst`) as input. Within the function, it uses a generator expression alongside the `sum` function to calculate the sum of squared integers in the list. 

Before performing this operation, the function filters the list to only include integer values that are multiples of 1 (i.e., integers), effectively removing any non-integer values (such as decimals). 

The function then returns the calculated sum of the squared integers. 

This code should be placed within a test suite and included within a `test_sum_squares` function to ensure the correctness of the `sum_squares` function.

For example:
```python
def test_sum_squares():
    # Test case 1
    assert sum_squares([1, 2, 3]) == 14

    # Test case 2
    assert sum_squares([1, 4, 9]) == 98

    # Test case 3
    assert sum_squares([1, 3, 5, 7]) == 84

    # Test case 4
    assert sum_squares([1.4, 4.2, 0]) == 29

    # Test case 5
    assert sum_squares([-2.4, 1, 1]) == 6
```

This test suite includes multiple test cases that cover a variety of scenarios which should hopefully validate the correctness of the `sum_squares` function. 
```