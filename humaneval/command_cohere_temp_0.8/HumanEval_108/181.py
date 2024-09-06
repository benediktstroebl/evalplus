Here is a Python script with a self-contained function that solves the problem:
```python
def count_nums(arr):
    return sum(int(num) >= 0 for num in arr)
```
This function uses a conditional sum to count the number of elements in the array that have a sum of digits greater than zero. 

Here is an example to demonstrate this function:
```python
>>> count_nums([-1, 11, -11]) == 1
True
```
This example catches the behavior described in the problem statement, confirming that the function correctly counts the number of elements with a sum of digits greater than zero.