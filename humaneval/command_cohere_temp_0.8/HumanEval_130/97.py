```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1 + n//2]
    else:
        return [tribonacci(n - 1)[i] + tribonacci(n - 2)[i] + tribonacci(n + 1)[i] for i in range(3)]
```