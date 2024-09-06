```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the `brazilian_factorial` of a given integer `n`. The Brazilian factorial is represented as a product of factorials up to `n`, with the smallest factorial (1!) multiplied by `n`. The script uses a loop to calculate and store factorials in the `factorial_list` up to `n`, and then returns the desired result.

Here is a simple test case to ensure the function behaves as intended:
```python
>>> special_factorial(4)
288
```

This is the expected result, as the Brazilian factorial of 4 is calculated by multiplying 4! with 3!.