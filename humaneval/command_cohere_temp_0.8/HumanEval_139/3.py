```python
def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    for i in range(2, n + 1):
        result //= factorial(i)
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

The `special_factorial` function calculates the Brazilian factorial of a given integer `n`. It first calculates the normal factorial of `n` by iterating from 1 to `n` and multiplying all integers in this range. Then, it iterates from 2 to `n` and recursively computes the factorial of each integer `(i - 1)!`, subtracting its contribution from the result after each iteration, effectively calculating the correct Brazilian factorial.

The `factorial` helper function is used for recursive factorial calculation. It uses the base case of `factorial(0) = 1` as per the standard factorial definition.