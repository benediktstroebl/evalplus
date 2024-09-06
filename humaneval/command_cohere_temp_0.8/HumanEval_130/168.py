```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0, 1, n // 2]
    else:
        return [1, 3, 2] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```
The function takes an integer n as input and returns a list of the first n + 1 numbers in the Tribonacci sequence. It checks if n is equal to 0, 1 or an even number, returning respectively [0], [1] or [0, 1, n//2]. In all other cases it returns [1, 3, 2] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1).