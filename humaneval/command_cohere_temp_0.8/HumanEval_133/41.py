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
    ceiling_lst = [round(x) for x in lst]
    return sum(x * x for x in ceiling_lst)
```

The function `sum_squares` serves the purpose of computing the sum of the squares of numbers after rounding each element in the list to the next highest integer. It achieves this by using two nested list comprehensions. The first comprehension rounds each element in the input list to the next highest integer. Meanwhile, the second comprehension calculates the square of each element in the rounded list and sums these values. This dual-comprehension approach ensures efficiency in both time and space complexity, making it an optimal solution for this problem.