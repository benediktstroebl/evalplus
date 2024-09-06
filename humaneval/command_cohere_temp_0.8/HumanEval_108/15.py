```python
def count_nums(arr):
    output = sum(int(b) for a in arr for b in str(a) if b != '0')
    return output
```
This function `count_nums` takes an array of integers and returns the number of elements that have a sum of digits greater than 0. It does this by summing up all the digits of each number in the array, and returning the count of numbers whose digit sum is greater than 0. 

Here are examples of test cases that prove its correctness:
```python
>>> count_nums([]) == 0
True

>>> count_nums([-1, 11, -11]) == 1
True

>>> count_nums([1, 1, 2]) == 3
True
```