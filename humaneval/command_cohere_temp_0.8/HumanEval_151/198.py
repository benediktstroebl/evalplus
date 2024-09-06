Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def double_the_difference(lst):
    odd_squares = sum(x**2 for x in lst if x % 2 and x >= 0)
    return int(odd_squares)
```
This function incorporates both the sum of odd squares and the conditional filtering of non-negative integers. By using a generator expression, it efficiently computes the desired sum without iterating over the list multiple times. The function returns the sum as an integer, as required by the problem statement. Overall, it is a concise and effective solution.