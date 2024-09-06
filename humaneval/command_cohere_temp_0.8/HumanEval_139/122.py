```python
def special_factorial(n):
    factorial_sequence = [1]
    for i in range(2, n+1):
        factorial_sequence.append(factorial_sequence[i-1] * i)
    return factorial_sequence[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem. It initializes a sequence `factorial_sequence` with `1` as the base factorial value. Then, it iterates from `2` up to `n` (the input value) and populates the sequence with calculated factorials using the formula `factorial_sequence[i-1] * i`. Finally, it returns the value of `factorial_sequence[n]`, which represents the Brazilian factorial for the given input `n`.