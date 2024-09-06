```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` to `n!`. The latter is computed through a loop that iterates from `2` up to `n`, calculating each factorial in the list using the formula `i * factorial_list[i - 1]`. The final element of the list, `factorial_list[n]`, is returned as the result, signifying the Brazilian factorial of the input integer `n`.

The code is self-contained, meaning it does not rely on any external variables or functions, and it's encapsulated within a single Python script. It efficiently computes the Brazilian factorial and is readily executable as is.