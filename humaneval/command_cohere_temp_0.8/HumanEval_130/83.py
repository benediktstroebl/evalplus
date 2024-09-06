```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1, n//2 + 1, tribonacci(n - 1)[1], tribonacci(n - 2)[1] + tribonacci(n - 1)[1] + tribonacci(n + 1)[1]]
    else:
        return [tribonacci(n - 1)[0], tribonacci(n - 2)[0], tribonacci(n - 1)[1], tribonacci(n - 2)[1] + tribonacci(n - 1)[1] + tribonacci(n + 1)[1]]
```