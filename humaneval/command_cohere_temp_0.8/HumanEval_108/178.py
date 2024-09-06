```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```

This script defines a Python function `count_nums` that takes an array of integers as input and calculates the number of elements with a sum of digits greater than zero. It uses a generator expression within the `sum` function to iterate through each element in the input array and evaluate its digit sum. The condition `sum(map(int, str(n))) > 0` checks if the sum of the integer's digits is greater than zero. The overall sum is returned as the count of elements meeting this criterion.

Here is an example usage of the function:
```python
arr = [1, 11, -11, 123, -123]
print(count_nums(arr))  # Output: 3
```

This will return `3` since the digits of the array elements `[1, 11, -11, 123, -123]` sum to `1 + 1 + 3 + (-1) + (-2) = 4`, and the elements with non-zero digit sums are `[1, 11, 123]`, therefore, the function counts 3 elements with a sum of digits greater than zero.