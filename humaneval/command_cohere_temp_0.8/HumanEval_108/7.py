```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```

This script defines a Python function `count_nums` that takes an array of integers as input and returns the number of elements in the array that have a sum of digits greater than zero. To achieve this, it employs a concise generator expression within the `sum` function, which assesses each number in the array via the `str(n)` conversion and `int` mapping to determine if its digits sum to a positive value.

For clarity, here's the breakdown of the generator expression:
- `map(int, str(n))`: This part transforms the string representation of the integer `n` into an iterable of individual digits via mapping. Each digit is then converted from a string to an integer using `int('d')`.
- `sum(...) > 0`: The `sum` function then calculates the sum of the integer digits. If the result is greater than zero, it means the number has a positive digit sum.

The function returns the count of such positive digit-sum numbers. This approach ensures efficiency and elegance in solving the problem.