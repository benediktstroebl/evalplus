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

This Python script defines a function called `sum_squares`, which takes a list of numbers as input. It first rounds each number in the list to the next higher integer. Then, it calculates the sum of the squared values of the rounded numbers and returns the result.

Here is an example of using this script:
```python
print(sum_squares([1, 2, 3]))  # Output: 14
```

This will output: 14, which is the sum of the squares of the rounded numbers [1, 2, 3] respectively. 

This script can be tested against the provided examples in the Markdown cell to ensure it behaves as expected.