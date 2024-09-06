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
    result = sum(x ** 2 for x in map(lambda x: round(x), lst))
    return result
```

The code uses `map()` and a lambda function to round each number in the list, `round(x)`, and then calculates the sum of squared integers using a generator expression, `x ** 2 for x in map(lambda x: round(x), lst)`. Finally, it returns the `result`. 

This approach ensures each list element is rounded up to the nearest integer before squaring and summing, as per the problem's instructions.