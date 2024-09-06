Here is a Python script with a self-contained function that solves the problem:
```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```
The function `count_nums` iterates through the array and calculates the sum of the digits for each integer. It returns the count of elements whose digit sum is greater than zero. This is achieved using a lambda expression and the `sum` function.

This solution is consistent with the given test cases and does not rely on any external variables or assumptions. Therefore, it is a self-contained solution that can be executed independently.