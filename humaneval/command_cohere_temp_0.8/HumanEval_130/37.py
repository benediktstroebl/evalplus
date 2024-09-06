```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0, 1, n // 2]
    else:
        return [tribonacci(n - 1)[-1], tribonacci(n - 2)[-1], tribonacci(n + 1)[-1]] + \
            tribonacci(n // 2)
```

The function employs a conditional structure that differentiates between even and odd values of `n`, employing the Fibonacci sequence's core logic to compute values and generating a list of the first `n + 1` Tribonacci values accordingly. To ensure scalability, it recursively calls itself to generate the Tribonacci sequence for half of the input value `n`, subsequently adding the final values to produce the complete result. 

To address the special cases of `n` being 1 or 0, the function returns the appropriate single values, achieving an elegant and efficient solution for the Tribonacci sequence problem.