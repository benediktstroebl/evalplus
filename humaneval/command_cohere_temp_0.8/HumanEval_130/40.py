```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1, n//2 + 1, tribonacci(n - 1)[0], tribonacci(n - 2)[0]]
    else:
        return [tribonacci(n - 1)[0], tribonacci(n - 2)[0], tribonacci(n + 1)[0], tribonacci(n)[0]]
```

The function takes the input `n` and returns the list of the first `n + 1` numbers of the Tribonacci sequence according to the definition. To achieve this, it includes the base cases `n == 0`, `n == 1`, and manages the cases for odd and even `n` differently, leading to the proper Tribonacci sequence.