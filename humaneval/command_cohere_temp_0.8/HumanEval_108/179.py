```python
def count_nums(arr):
    return sum(int(num) >= 0 for num in arr)
```
The `count_nums` function uses a short lambda expression inside `sum`. This expression checks if the integer `num` is non-negative, effectively checking if its digit sum is non-negative too. Using this, the function filters out non-negative numbers from the array and returns their count, answering the question asked. 

The test cases provided in the problem statement are reflected below:
```python
>>> count_nums([]) == 0
True

>>> count_nums([-1, 11, -11]) == 1
True

>>> count_nums([1, 1, 2]) == 3
True
```