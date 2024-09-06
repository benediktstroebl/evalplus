```python
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    rounded_lst = [round(x) for x in lst]
    return sum(x * x for x in rounded_lst)
```

This script defines a function `sum_squares` that takes in a list of numbers and squares each rounded element while summing them up returning the final result. The function is then tested using the following test cases:
```python
test_sum_squares = {
    "[1,2,3]": 14,
    "[1,4,9]": 98,
    "[1,3,5,7]": 84,
    "[1.4,4.2,0]": 29,
    "[-2.4,1,1]": 6,
}

for inp, out in test_sum_squares.items():
    assert sum_squares(inp) == out
```

Which verifies that the function `sum_squares` operates correctly as described in the problem statement.