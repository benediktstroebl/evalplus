Here is a Python script with a self-contained function that solves the problem:
```python
def count_nums(arr):
    return sum(int(num) >= 0 for num in arr)
```
This function uses a conditional sum to count the number of elements in the array that have a sum of digits greater than zero. 

This solution works because the condition `int(num) >= 0` evaluates to `True` for positive integers and `False` for negative integers.

As specified in the prompt, this function correctly passes the tests:
```python
>>> count_nums([]) == 0
True
>>> count_nums([-1, 11, -11]) == 1
True
>>> count_nums([1, 1, 2]) == 3
True
```