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
The function takes an input integer `n` and returns a list of the first `n + 1` numbers in the Tribonacci sequence according to the definition provided in the prompt. This is achieved through recursive and non-recursive branches depending on the value of `n`.