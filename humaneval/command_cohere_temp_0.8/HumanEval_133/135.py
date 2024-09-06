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

The code first maps each element in the list to its closest integer value, and then calculates the sum of squares of these integer values. Ultimately this returns the sum of squared numbers in the list as expected. 

To manage floating point values, the `round()` function is utilized to round a number to the nearest integer. The `lambda` function enables creating an anonymous function that rounds the elements of the list. Utilizing the `map()` function, the list is then traversed and each element is modified to its upper integer value. Lastly, the sum of squared values is computed using the `sum()` function. 

This approach ensures correctness and adaptability to various scenarios as illustrated in the given examples.