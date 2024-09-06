```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

The code uses a for loop to iterate through each index and value in the input list `lst`. By using the `enumerate` function, the code instantly has access to both the index (`i`) and value (`num`) of each list element.

For each element, the code checks whether the index is divisible by 3 with the condition `i % 3 == 0`. If true, the code will add the square of the integer to the `result` variable.

If the index is divisible by 4, but not divisible by 3 (i.e., `i % 4 == 0` and `i % 3 != 0`), the code will add the cube of the integer to the `result` variable.

Finally, the code returns the `result` variable, which at the end will contain the sum of all entries squared or cubed as described in the problem.

This Python script solves the problem using a single, self-contained `sum_squares` function, which follows the problem statement and passes the provided tests.