Here is a Python script with a self-contained function that solves the problem:
```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```
The function `count_nums` iterates through the array and calculates the sum of the digits for each element. It returns the number of elements that have a sum of digits greater than 0. The parser tests are done with the condition `sum(sum(map(int, str(n))) > 0 for n in arr)`.