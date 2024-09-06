```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1] + [n // 2] * (n // 2)
    else:
        return [1] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```
The function takes an input of type integer `n` and returns a list of the first `n + 1` numbers in the Tribonacci sequence. This is achieved via basic if-else statements that properly classify the type of sequence and return the appropriate list. The if-else statements cater to the different possible inputs like the base case of `n == 0` or `n == 1`, as well as the different types of sequences (odd, even). The odd type particularly is recursive as it calls itself with `tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)`.