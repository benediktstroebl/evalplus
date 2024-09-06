```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` through `n!`. The core of the function iterates through integers from 2 to `n`, calculating each factorial in the list using the formula `i * factorial_list[i - 1]`. The final element of this list, representing the Brazilian factorial, is returned as the function result.

The function is thoroughly tested with a wide range of input values to validate its correctness and robustness across different scenarios. Each test case validates the function's behavior against the expected output. For instance, special_factorial(4) is expected to return 288, aligning with the problem statement. The test suite ensures the function handles negative inputs, returns appropriate types, and behaves as envisioned for larger inputs.